#include <string>
#include <iostream>

using namespace std;

int main()
{
    string str;
    cout << "문자열 입력: ";
    getline(cin, str);
    cout << "입력된 문자열: " << str << endl;
    return 0;
}