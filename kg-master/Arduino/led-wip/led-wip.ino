  
int led[6] = {2, 3, 4, 5, 6, 7};
const int wip = A0;

int cur = 0;
int pre = 0;

void setup()
{
 /*
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
 */
  for (int i = 0; i < 6; i++)
    pinMode(led[i], OUTPUT);
  
  Serial.begin(9600);
}

void loop()
{
	int val = analogRead(wip);
  	 
  	
  	Serial.println(val);
  	cur = map(val, 0, 1023, 0 ,5);
  if(cur != pre){
    pre = cur;
    for (int i = 0; i <cur; i++){
      digitalWrite(led[i],HIGH);}
  for (int i = cur; i<5; i++)
    digitalWrite(led[i], LOW);
  /*
  	digitalWrite(led1, LOW);
  	digitalWrite(led2, LOW);
  	digitalWrite(led3, LOW);
  	digitalWrite(led4, LOW);
  	digitalWrite(led5, LOW);
  	digitalWrite(led6, LOW);
  	*/