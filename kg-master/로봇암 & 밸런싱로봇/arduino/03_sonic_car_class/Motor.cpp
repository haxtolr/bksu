// Motor.cpp
#include "Motor.h"

Motor::Motor(int pinA, int pinB) {
  this->pinA = pinA;
  this->pinB = pinB;
  pinMode(pinA, OUTPUT);
  pinMode(pinB, OUTPUT);
}

void Motor::setSpeed(int speed) {
  this->speed = speed;
}

void Motor::forward() {
  analogWrite(pinA, speed);
  analogWrite(pinB, 0);
}

void Motor::backward() {
  analogWrite(pinA, 0);
  analogWrite(pinB, speed);
}

void Motor::stop() {
  analogWrite(pinA, 0);
  analogWrite(pinB, 0);
}
