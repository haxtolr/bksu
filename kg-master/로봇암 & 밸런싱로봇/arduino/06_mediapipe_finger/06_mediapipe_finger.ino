#define PIN_LED 9


void setup() {

  Serial.begin(115200);
  pinMode(PIN_LED, OUTPUT);
}

void loop() {

  if (Serial.available())
  {
    int led = Serial.read();
    led  = constrain(led, -1, 255);
    analogWrite(PIN_LED, led);
  }
}
