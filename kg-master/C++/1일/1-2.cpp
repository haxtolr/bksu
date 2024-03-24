// 반지름을 입력 받고, 원의 넓이를 계산하여 출력하는 프로그램을 작성하세요. (원주율은 3.14로 가정합니다.)

#include <iostream>

int main()
{
    float radius;
    double area;

    std::cout << "반지름: ";
    std::cin >> radius;
    area = 3.14 * radius * radius;
    std::cout << "원의 넓이: " << area << std::endl;
    return 0;
}