#include "LMotorController.h"

#define MIN_ABS_SPEED 20

//MOTOR CONTROLLER
int ENA = 3;
int IN1 = 4;
int IN2 = 5;
int IN3 = 7;
int IN4 = 8;
int ENB = 9;

LMotorController motorController(ENA, IN1, IN2, ENB, IN3, IN4, 1, 1);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Start...");

}

void loop() {
  // put your main code here, to run repeat`edly:
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
