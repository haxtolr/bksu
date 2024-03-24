#include <DHT.h>
#include <SoftwareSerial.h>

DHT dht (A0, DHT11);
SoftwareSerial blue(2, 3);

void setup() {
  blue.begin(9600);
  dht.begin();
}

void loop() {
  float temper = dht.readTemperature();
  blue.println("t" + String(temper));
  delay(1000);
  float humid = dht.readHumidity();
  blue.println("h" + String(humid));
  delay(1000);
}
