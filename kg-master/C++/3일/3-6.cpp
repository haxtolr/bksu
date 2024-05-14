#include <iostream>

using namespace std;

int main()
{
    int arr[5];


    for (int i = 0; i < 5; i++){
        cout << "배열 입력 : ";
        cin >> arr[i];
    }
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << endl;
    }
    return 0;
}