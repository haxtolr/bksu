#include <Servo.h>

#define TRIGGER_PIN 9
#define ECHO_PIN 10
#define SERVO_PIN 11

Servo servo;

void setup() {
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(9600);
  servo.attach(SERVO_PIN);
}

void loop() {
  long duration, distance;
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);

  distance = (duration / 2) / 29.1;
  Serial.println(distance);
  if (distance <60) { 
    
    servo.write(0); //파란불
    delay(6000);
    servo.write(180); //빨간불
    delay(6000);
  }
  distance = 80;
  servo.write(180); //빨간불
   
  }
