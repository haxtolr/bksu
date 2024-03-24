#define PIN_MA1A 6
#define PIN_MA1B 5

#define PIN_MB1A 9
#define PIN_MB1B 10

#define pin_ir_l 4
#define pin_ir_r 8

int iSpeed = 125;
int leftWheelSpeed = iSpeed;
int WHEEL_DIFF_VALUE = 0;
int rightWheelSpeed = leftWheelSpeed + WHEEL_DIFF_VALUE;

#define LINE 1
#define NO_LINE 0

#define GET_IR_L digitalRead(pin_ir_l)
#define GET_IR_R digitalRead(pin_ir_r)

void setup() {
  // 모터 핀
  pinMode(PIN_MA1A, OUTPUT);
  pinMode(PIN_MA1B, OUTPUT);
  pinMode(PIN_MB1A, OUTPUT);
  pinMode(PIN_MB1B, OUTPUT);

  pinMode(pin_ir_l, INPUT);
  pinMode(pin_ir_r, INPUT);

  Serial.begin(9600);

}

void loop() {
  Serial.println(GET_IR_L);
  Serial.println(GET_IR_R);
  soniCar();
}


void soniCar()
{
  if (GET_IR_L == LINE && GET_IR_R == NO_LINE)
  {
    left();
    //Serial.println("right");
  }
  else if (GET_IR_R == LINE && GET_IR_L == NO_LINE)
  {
    right();
    //Serial.println("left");
  }
  else if (GET_IR_L == LINE && GET_IR_R == LINE)
  {
    stop();
    //Serial.println("backward");
  }
  else if (GET_IR_L == NO_LINE && GET_IR_R == NO_LINE)
  {
    forward();
    //Serial.println("fd");
  }

}
// void updateSpeed() {
//   sensors_event_t a, g, temp;
//   mpu.getEvent(&a, &g, &temp);

//   long gyro = round(g.gyro.z * 10);
//   Serial.print("Gyro.Z :");
//   Serial.println(round(g.gyro.z * 10));
  
//   if (gyro > 0)
//     WHEEL_DIFF_VALUE--;
//   else
//     WHEEL_DIFF_VALUE++;
    
// }

void carMove(int aa, int ab, int ba, int bb) {
  analogWrite(PIN_MA1A, aa);
  analogWrite(PIN_MA1B, ab);
  analogWrite(PIN_MB1A, ba);
  analogWrite(PIN_MB1B, bb);
}

void forward() {
  carMove(leftWheelSpeed, 0, rightWheelSpeed, 0);
}

void backward() {
  carMove(0, leftWheelSpeed, 0, rightWheelSpeed);
}

void left() {
  carMove(0, 20, 90, 0);
}
void right() {
  carMove(90, 0, 00, 0);
}
void stop() {
  carMove(0, 0, 0, 0);
}

// long getDistance()

// {
//   digitalWrite(PIN_SONIC_TRIG, LOW);
//   delayMicroseconds(2);
//   digitalWrite(PIN_SONIC_TRIG, HIGH);
//   delayMicroseconds(10);
//   digitalWrite(PIN_SONIC_TRIG, LOW);


//   long duration = pulseIn(PIN_SONIC_ECHO, HIGH);
//   long distance = (duration / 2) / 29.1;
//   return distance;
// }
