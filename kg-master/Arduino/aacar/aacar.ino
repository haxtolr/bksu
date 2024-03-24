#include <SoftwareSerial.h>

#define tx 2
#define rx 3

SoftwareSerial blue(2, 3);

#define BWHEEL 5
#define BSPEED 6 //

#define AWHEEL 11
#define ASPEED 10

#define led 7

const int trig = 9;
const int echo = 8;

void control(int c, int distace);

void setup() {
  Serial.begin(9600);
  while(!Serial)
    {;}
  blue.begin(9600);

  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  
  pinMode(led, OUTPUT);
  pinMode(ASPEED, OUTPUT);
  pinMode(AWHEEL, OUTPUT);
  pinMode(BSPEED, OUTPUT);
  pinMode(BWHEEL, OUTPUT);
}
void loop() {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(2);
  digitalWrite(trig, LOW);

  long duration = pulseIn(echo, HIGH);
  long distace = (duration/2) / 29.1;

    if(blue.available())
   {
    int c = blue.read();

    control(c, distace);
    if (c != 's')
      digitalWrite(led, HIGH);
    else
      digitalWrite(led, LOW);
    Serial.write(blue.read());
   }
    if(Serial.available())
      blue.write(Serial.read()); 
    if (distace < 15)
    {
      analogWrite(BSPEED, 0);   //앞
      analogWrite(BWHEEL, 0);
      analogWrite(ASPEED, 0);   //앞
      analogWrite(AWHEEL, 0);
    }
}

void control(int c, int distace)
{
  if (c == 'u')
  {
    analogWrite(BSPEED, 0);   //앞
    analogWrite(BWHEEL, 104);
    analogWrite(ASPEED, 0);   //앞
    analogWrite(AWHEEL, 104);
  }
  
  if (c == 'd')
  {
    analogWrite(BSPEED, 104);  
    analogWrite(BWHEEL, 0);
    analogWrite(ASPEED, 104);  
    analogWrite(AWHEEL, 0); 
  }
  if (c == 'l')
  {
    analogWrite(BSPEED, 0);   
    analogWrite(BWHEEL, 90);
    analogWrite(ASPEED, 0);   
    analogWrite(AWHEEL, 204);
  }
  if (c == 'r')
  {
    analogWrite(BSPEED, 0);   
    analogWrite(BWHEEL, 204);
    analogWrite(ASPEED, 0);   
    analogWrite(AWHEEL, 90);
  }
  if (c == 'f')
  {
    analogWrite(BSPEED, 0);   
    analogWrite(BWHEEL, 205);
    analogWrite(ASPEED, 0);   
    analogWrite(AWHEEL, 205);
  }
  if (c == 't')
  {
    analogWrite(BSPEED, 0);   
    analogWrite(BWHEEL, 0);
    analogWrite(ASPEED, 0);   
    analogWrite(AWHEEL, 105);
  }
  
  if (c == 's')
  {
    analogWrite(BSPEED, 0);   //앞
    analogWrite(BWHEEL, 0);
    analogWrite(ASPEED, 0);   //앞
    analogWrite(AWHEEL, 0);
  }
}