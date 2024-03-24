#include <Servo.h>

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SPI.h>
#include <Wire.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);



const int basePin = 4;
const int shoulderPin = 5;
const int upperarmPin = 6;
const int forearmPin = 7;

const int servoInitAngle = 90;

Servo base;
Servo shoulder;
Servo upperarm;
Servo forearm;

void setup() {
  Serial.begin(9600);
  
  base.attach(basePin);
  shoulder.attach(shoulderPin);
  upperarm.attach(upperarmPin);
  forearm.attach(forearmPin);

  base.write(servoInitAngle);
  shoulder.write(servoInitAngle + 3);
  upperarm.write(servoInitAngle + 5);
  forearm.write(servoInitAngle - 3);

  //

   if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  Serial.println("oled found")
  
  display.clearDisplay();
  display.display();
  
}

void loop() {
  display.clearDisplay();
  

}
