// Motor.h
#ifndef Motor_h
#define Motor_h

#include <Arduino.h>

class Motor {
  private:
    int pinA;
    int pinB;
    int speed;

  public:
    Motor(int pinA, int pinB);
    void setSpeed(int speed);
    void forward();
    void backward();
    void stop();
};

#endif
