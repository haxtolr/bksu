int speed = 10;
int wheel = 9;
int trig = 6;
int echo = 5;
int val = 127;

void setup()
{
  Serial.begin(9600);
  pinMode(speed, OUTPUT);
  pinMode(wheel, OUTPUT);
  digitalWrite(wheel, LOW);
  analogWrite(speed, 0);
  //
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

void loop()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  
  long duration;
  long distance;

  duration = pulseIn(echo, HIGH);
  distance = (duration/2) / 29.1;

  Serial.print(distance);
  Serial.println(" cm");
  //
  if (Serial.available() > 0){
    char c = Serial.read();
    if (c == 'R')
    {
     digitalWrite(wheel, LOW);
     analogWrite(speed, distance/10);
    } 
    else if (c == 'L')
    {
     digitalWrite(wheel, HIGH);
     analogWrite(speed, distance);
    }
    else if (c == 'S')
   {
     digitalWrite(wheel, LOW);
     analogWrite(speed, 0);
   }
  }
}