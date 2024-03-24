#include "LMotorController.h"

#define MIN_ABS_SPEED  120

//MOTOR CONTROLLER
int ENA = 5;
int IN1 = 6;
int IN2 = 7;
int IN3 = 8;
int IN4 = 9;
int ENB = 10;

LMotorController motorController(ENA, IN1, IN2, ENB, IN3, IN4, 1, 1);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Start...");

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("move");
  motorController.move(200);
  delay(3000);

  Serial.println("stop");
  motorController.stopMoving();  
  delay(3000);

  Serial.println("move back");
  motorController.move(-200);  
  delay(3000);

  Serial.println("turn left");
  motorController.turnLeft(200, false);  
  delay(3000);

}