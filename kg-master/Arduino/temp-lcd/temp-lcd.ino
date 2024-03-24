
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 7, 6, 5, 4);
int temp = A0;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("temp : ");
}

void loop()
{
  lcd.setCursor(0, 1);
  int reading = analogRead(temp);
  float mill = (reading * 5.0) / 1024.0;
  float cent = (mill - 0.5) * 100;
  lcd.print(cent);
  Serial.print("temp: ");
  Serial.println(cent);
  delay(600);
}