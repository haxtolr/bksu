#include <Servo.h>

const int SERVO = 9;
Servo servo;
const int trig = 6;
const int echo = 5;

void setup() {
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  servo.write(0);
  }

void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long duration = pulseIn(echo, HIGH);
  long distace = (duration/2) / 29.1;

  Serial.print(distace);
  Serial.println(" cm");

  if (distace < 10)
  {
    servo.write(180);
    delay(1000);
  }
  if (distace > 10)
  {
    servo.write(0);
    delay(1000);
  }
}

