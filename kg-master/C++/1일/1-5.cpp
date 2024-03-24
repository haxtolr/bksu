#include <iostream>
#include <string>

using namespace std;

void check_num();
void big_num();
void min_num();

int main()
{
    int num;

     cout << "미션 : ";
     cin >> num;
     switch (num)
     {
     case 1:
        check_num();     
        break;
     case 2:
        big_num();
        break;
     case 3:
        min_num();
        break;
     default:
        break;
     }
}

void check_num()
{
    int a;
    int b;
    int c;
    string result;

    cout << "수를 입력하세요" << endl;
    cin >> a;

    b = a%2;
    (b == 0) ? result = "짝수" : result = "홀수";
    cout << result << endl;

    return ;
}

void big_num()
{
    int a;
    int b;

    cout << "두 수를 입력하세요" << endl;
    cin >> a >> b;
    (a > b) ? cout << a << endl : cout << b << endl;
}

void min_num()
{
    int a;
    int b;
    int c;

    cout << "세 수를 입력하세요" << endl;
    cin >> a >> b >> c;
    (a < b) ? (a < c) ? cout << a << endl : cout << c << endl : (b < c) ? cout << b << endl : cout << c << endl;
}