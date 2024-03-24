// UltrasonicSensor.h
#ifndef UltrasonicSensor_h
#define UltrasonicSensor_h

#include <Arduino.h>

class UltrasonicSensor {
  private:
    int trigPin;
    int echoPin;

  public:
    UltrasonicSensor(int trigPin, int echoPin);
    long getDistance();
};

#endif
