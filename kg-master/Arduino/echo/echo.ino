const int trig = 12;
const int echo = 11;

void setup()
{
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  Serial.begin(115200);
}

void loop()
{
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long duration = pulseIn(echo, HIGH);
  long distace = (duration/2) / 29.1;

  Serial.print(distace);
  Serial.println(" cm");
}