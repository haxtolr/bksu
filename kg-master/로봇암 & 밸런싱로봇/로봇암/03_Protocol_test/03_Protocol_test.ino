void setup() {
  Serial.begin(115200);

}

void loop() {
  int baseA, shoulderA, uppeararmA, forearmA;

  while(Serial.available() > 0)
  {
    baseA = Serial.parseInt();
    shoulderA = Serial.parseInt();
    uppeararmA = Serial.parseInt();
    forearmA = Serial.parseInt();

    if (Serial.read() == 'd'){
      Serial.println(("Received Signal"));
    }
    
  String base = "base : " + String(baseA);
  String shoulder = "shoulder : " + String(shoulderA);
  String upperarm = "uppeararm : " + String(uppeararmA);
  String forearm = "forearm : " + String(forearmA);

  Serial.println(base);
  Serial.println(shoulder);
  Serial.println(upperarm);
  Serial.println(forearm);
  }
}
