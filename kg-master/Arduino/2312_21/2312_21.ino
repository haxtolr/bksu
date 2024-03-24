#include <Bounce2.h>

Bounce debounce_r = Bounce();
Bounce debounce_b = Bounce();

int but_r = 10;
int but_b = 11;
int ledr = 5;
int ledb = 6;

void setup() {
  Serial.begin(9600);
  pinMode(ledr, OUTPUT);
  pinMode(ledb, OUTPUT);
  //pinMode(but_r, INPUT_PULLUP);
  //pinMode(but_b, INPUT_PULLUP);
  debounce_b.attach(but_b, INPUT_PULLUP);
  debounce_r.attach(but_r, INPUT_PULLUP);
  debounce_b.interval(50);
  debounce_r.interval(50);
}

void loop() {
  debounce_b.update();
  debounce_r.update();
  if (debounce_b.fell())
  {
    Serial.println("R");
    digitalWrite(ledb, HIGH);
  }
  if (debounce_b.rose())
  {
    digitalWrite(ledb, LOW);
  }
  if (debounce_r.fell())
  {
    Serial.println("L");
    digitalWrite(ledr, HIGH);
  }
  if (debounce_r.rose())
  {
    digitalWrite(ledr, LOW);
  }

}