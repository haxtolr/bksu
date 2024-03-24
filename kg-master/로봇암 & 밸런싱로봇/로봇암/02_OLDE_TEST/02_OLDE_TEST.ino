#include <Servo.h>

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SPI.h>
#include <Wire.h>

#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64  // OLED display height, in pixels

#define OLED_RESET -1        // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C  ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


void setup() {
  Serial.begin(9600);

  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;)
      ;  // Don't proceed, loop forever
  }

  Serial.println("oled found");

  display.clearDisplay();
  display.display();
}

int Angle = 0;

void loop() {
  display.clearDisplay();
  if (Angle >= 180)
    Angle = 0;
  Angle += 10;
  String base = "base : " + String(Angle);
  String shoulder = "shoulder : " + String(Angle);
  String upperarm = "uppeararm : " + String(Angle);
  String forearm = "forearm : " + String(Angle);

  display.setTextSize(1.5);
  display.setTextColor(SSD1306_BLACK, SSD1306_WHITE);
  display.setCursor(0,0);
  display.println("RObot Arm Move");
  display.setTextColor(SSD1306_WHITE);
  display.println("-------------");
  display.println(" ");
  
  display.setTextSize("1");
  display.println(base);
  display.println(shoulder);
  display.println(upperarm);
  display.println(forearm);
  display.println(" ");

  display.display();
  delay(500);
  }