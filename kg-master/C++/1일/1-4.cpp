#include <iostream>
#include <string>

using namespace std;

int main()
{
    char c;
    cout << " 입력하세요 : "<<endl;
    cin >> c;

    c = tolower(c);
    switch (c)
    {
    case 'w' :
        cout << "위로 이동"<<endl;
        break;
    case 'a':
        cout << "왼쪽으로 이동"<<endl;
        break;
    case 's':
        cout << "아래로 이동"<<endl;
        break;
    case 'd':
        cout << "오른쪽으로 이동"<<endl;
        break;
    }
}