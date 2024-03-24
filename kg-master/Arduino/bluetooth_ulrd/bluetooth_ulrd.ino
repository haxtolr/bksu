#include <SoftwareSerial.h>

#define tx 2
#define rx 3

SoftwareSerial blue(2, 3);

void setup() {
  Serial.begin(9600);
  while(!Serial)
    {;}
  blue.begin(9600);
  blue.println("hi ");
  Serial.println("good");
}

void loop() {
  if(blue.available())
  {
    Serial.write(blue.read());
  }
  if(Serial.available())
    blue.write(Serial.read());
}
