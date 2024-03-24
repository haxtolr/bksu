#include <SoftwareSerial.h>
#include <stdlib.h>

#define tx 2
#define rx 3
char ser = 0;
char ble = 0;
int wip = A0;

int led = 11;

SoftwareSerial HC06(tx, rx);

void setup() {
  Serial.begin(9600);
  HC06.begin(9600);

  pinMode(led, OUTPUT);
}

void HC06proc()
{
  if(Serial.available() > 0)
  {
    ser = Serial.read();
    HC06.write(ser);
    digitalWrite(led, HIGH);
  }
  if(HC06.available()>0)
  {
    ble =HC06.read();
    Serial.write(ble);
    digitalWrite(led, LOW);
  }
}

void loop() {
  int val = analogRead(wip); 
  HC06proc();
  HC06.println(val);
}