#include <Servo.h>

Servo servo;
const int trig = 6;
const int echo = 5;

const int r = A5;
const int g = A3;
const int b = A4;

void setup() {
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  servo.attach(9);
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
    analogWrite(g, 255);
    analogWrite(r, 0);
    delay(100);
  }
  if (distace > 10)
  {
    analogWrite(g, 0);
    analogWrite(r, 255);
    servo.write(0);
    delay(100);
  }
}
