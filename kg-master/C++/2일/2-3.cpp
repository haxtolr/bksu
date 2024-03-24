#include <iostream>
#include <string>
using namespace std;

//상속 + 오버라이딩
//car 클래스

class Car {
private: 
   int num;
   double gas;
public:
   Car();
   void setCar(int n, double g);
   void printer();
};

//Racing Car 클래스 선언
class RacingCar : public Car
{
private:
   int course;
public:
   RacingCar();
   void setCourse(int c);
   void printer();
};

int main() {

   RacingCar rcCar1; 
   rcCar1.setCar(1234, 33.3);
   rcCar1.setCourse(7);

   rcCar1.printer(); 
   return 0;
}

Car::Car() {
   num = 0;
   gas = 0.0;
   cout << "자동차 탄생\n";
}

void Car::setCar(int n, double g)
{
   num = n;
   gas = g;
   cout << "차량 번호: " << n << endl;
   cout << "연료량: " << g << endl;
}

void Car::printer()
{
   cout << "차량번호:" << num << endl;
   cout << "연료량:" << gas << endl;
}

void RacingCar::printer()
{
   cout << "차량번호:" << num << endl;
}

RacingCar::RacingCar()
{
   course = 0;
   cout << "레이싱카 탄생\n";
}

void RacingCar::setCourse(int c)
{
   course = c;
   cout << "코스 번호:" << course << endl;
}