#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64  // OLED display height, in pixels

#define OLED_RESET -1        // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C  ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#include <Servo.h>

int basePin = 4;
int shoulderPin = 5;
int upperarmPin = 6;
int forearmPin = 7;

const int servoInitAngle = 90;

int baseAngle = servoInitAngle;
int shoulderAngle = servoInitAngle;
int upperarmAngle = servoInitAngle;
int forearmAngle = servoInitAngle;

Servo base;
Servo shoulder;
Servo upperarm;
Servo forearm;

int baseStatus = 1;
int shoulderStatus = 1;
int upperarmStatus = 1;
int forearmStatus = 1;

#define PIN_JOINT_READ_BUTTON 8
#define PIN_JOINT_JOYSTICK_MODE 2
#define but 12
#define PIN_LED 13

bool isJoystickMode = false;
int done = 0;

int servoParallelControl(int thePos, Servo theServo, int speed) {
  int startPos = theServo.read();
  int newPos = startPos;

  if (startPos < (thePos)) {
    newPos = newPos + 1;
    theServo.write(newPos);
    delay(speed);
    return 0;
  } else if (newPos > (thePos)) {
    newPos = newPos - 1;
    theServo.write(newPos);
    delay(speed);
    return 0;
  } else {
    return 1;
  }
}


void setup() {
  Serial.begin(115200);
  pinMode(PIN_JOINT_READ_BUTTON, INPUT_PULLUP);
  pinMode(PIN_JOINT_JOYSTICK_MODE, INPUT_PULLUP);
  pinMode(PIN_LED, OUTPUT);
  pinMode(but, INPUT_PULLUP);

  attachInterrupt(INT0, ISRJoystickMode, LOW);

  base.attach(basePin);
  shoulder.attach(shoulderPin);
  upperarm.attach(upperarmPin);
  forearm.attach(forearmPin);

  base.write(servoInitAngle);
  shoulder.write(servoInitAngle);
  upperarm.write(servoInitAngle);
  forearm.write(servoInitAngle);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;)
      ;  // Don't proceed, loop forever
  }
  // Clear the buffer
  Serial.println("oled found!");
  display.clearDisplay();
  display.display();
}

void ISRJoystickMode() {
	static unsigned long prev = 0;

	if (millis() - prev > 50 && digitalRead(PIN_JOINT_JOYSTICK_MODE) == LOW) {
		isJoystickMode = !isJoystickMode;
		prev = millis();
	}
	if (isJoystickMode) {
		digitalWrite(PIN_LED, HIGH);
	} else {
		digitalWrite(PIN_LED, LOW);
	}
}

//조이스틱 모드 체크, 값을 읽어서 전역변수 angle값 수정
void checkJoystickMode() {
	if (isJoystickMode) {
		baseAngle = map(analogRead(A1), 0, 1023, 5, 175);
		shoulderAngle = map(analogRead(A0), 0, 1023, 5, 175);
		upperarmAngle = map(analogRead(A3), 0, 1023, 5, 175);
		forearmAngle = map(analogRead(A2), 0, 1023, 5, 175);
		
		done = 0;
	}
}

//D8 버튼이 눌렸을때 서보 값을 읽어서 OLED에 보여주는 함수
void checkJointReadButton() {
	if (digitalRead(PIN_JOINT_READ_BUTTON) == LOW) 
	{
		isJoystickMode = false;

		baseAngle = base.read();
		shoulderAngle = shoulder.read();
		upperarmAngle = upperarm.read();
		forearmAngle = forearm.read();

		displayOLED();
		while (!digitalRead(PIN_JOINT_READ_BUTTON))
			;
	}
}

void displayOLED() {
	String baseStr = " base     : " + String(baseAngle);
	String shoulderStr = " shoulder : " + String(shoulderAngle);
	String upperarmStr = " upperarm : " + String(upperarmAngle);
	String forearmStr = " forearm  : " + String(forearmAngle);

	display.clearDisplay();
	display.setTextSize(1);  // Normal 1:1 pixel scale
	display.setTextColor(SSD1306_BLACK, SSD1306_WHITE);  // Draw 'inverse' text

	display.setCursor(0, 0);  // Start at top-left corner
	display.println(" Robot Arm Move");
	display.setTextColor(SSD1306_WHITE);  // Draw white text
	display.println(" --------------");
	display.println(" ");
	display.setTextSize(1);  //  1:1 pixel scale
	display.println(baseStr);
	display.println(shoulderStr);
	display.println(upperarmStr);
	display.println(forearmStr);
	display.println("\n");  // OLED 에 마지막 줄이 안 보여서 넣어준 것임

	display.setCursor(0, 0);  // Start at top-left corner
	display.display();
	delay(100);
}

//서보모터 움직이는 부분
void moveJoints()
{
	if (isJoystickMode) 
	{
		baseStatus = servoParallelControl(baseAngle, base, 20);
		shoulderStatus = servoParallelControl(shoulderAngle, shoulder, 20);
		upperarmStatus = servoParallelControl(upperarmAngle, upperarm, 20);
		forearmStatus = servoParallelControl(forearmAngle, forearm, 20);
	}
	else 
	{
		while (done == 0) 
		{
    	baseStatus = servoParallelControl(baseAngle, base, 20);
    	shoulderStatus = servoParallelControl(shoulderAngle, shoulder, 20);
    	upperarmStatus = servoParallelControl(upperarmAngle, upperarm, 20);
    	forearmStatus = servoParallelControl(forearmAngle, forearm, 20);

      	if (baseStatus == 1 && shoulderStatus == 1 && upperarmStatus == 1 && forearmStatus == 1)
			done = 1;
    	}
	}
}

void ft_send() {
  Serial.print(baseAngle);
  Serial.print(",");
  Serial.print(shoulderAngle);
  Serial.print(",");
  Serial.print(upperarmAngle);
  Serial.print(",");
  Serial.print(forearmAngle);
  Serial.println("d");
}

void loop() 
{
  checkJointReadButton();
	checkJoystickMode();
  if (digitalRead(but) == LOW && digitalRead(PIN_JOINT_READ_BUTTON) == HIGH) 
  {
    ft_send();
    delay(1000);
  }
  if (Serial.available() > 0) 
	{
    //10,30,40,50d
    //90,90,90,90d
    //45,75,75,75d

    baseAngle = Serial.parseInt();
    shoulderAngle = Serial.parseInt();
    upperarmAngle = Serial.parseInt();
    forearmAngle = Serial.parseInt();

  if (Serial.read() == 'd') {
     Serial.println("received signal");
  }

	displayOLED();
    
	done = 0;
  	}
	moveJoints();
}