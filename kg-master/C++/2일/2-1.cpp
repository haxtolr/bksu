#include <iostream>
#include <string>

using namespace std;

void ft_swap(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;

    return ;
}

int main()

{
    int a;
    int b;

    cout << "a : ";
    cin >> a;

    cout << "b : ";
    cin >> b;
    
    ft_swap(&a, &b);

    cout << "a : " << a << endl;
    cout << "b : " << b << endl;

    return 0;
}