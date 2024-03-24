#include <SoftwareSerial.h>
#include <DHT.h>

#define tx 2
#define rx 3
#define dhtpin 4
#define dhttype DHT11

SoftwareSerial HC06(tx, rx);
DHT dht (dhtpin, dhttype);

char ser = 0;
char ble = 0;
float temp = 0;
float humi = 0;

void setup() {
  Serial.begin(9600);
  HC06.begin(9600);
  dht.begin();
}

void HC06proc(){
  if(Serial.available()>0)
  {
    ser = Serial.read();
    HC06.write(ser);
  }
  if(HC06.available()>0)
  {
    ble = HC06.read();
    HC06.write(ble);
  }
}

void DHTproc()
{
  temp = dht.readTemperature();
  humi = dht.readHumidity();

  if(isnan(temp) || isnan(humi)){
    Serial.println("FAIL TO READ DHT ");
    return;
  }
}

void DataPrint()
{
  Serial.print("Tem: ");
  Serial.print(temp);
  Serial.print(" ℃");
  Serial.print("\t");
  Serial.print(humi);
  Serial.println(" %");

 
  HC06.print("Tem: ");
  HC06.print(temp);
  HC06.print(" ℃");
  HC06.print("\t");
  HC06.print(humi);
  HC06.println(" %");
 
}

void loop() {
  HC06proc();
  DHTproc();
  DataPrint();
  delay(2000);
}
