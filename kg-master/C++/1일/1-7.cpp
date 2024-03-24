#include <iostream>

using namespace std;

void ft_3();
void ft_sqrt();
void ft_prime();

int main()
{
    int n;
    int i;

    cout << "미션 입력 : ";
    cin >> n;
    
    if (n == 1)
    {
        ft_3();
    }
    else if (n == 2)
    {
        ft_sqrt();
    }
    else if (n == 3)
    {
        ft_prime();
    }
    else
    {
        cout << "잘못된 미션입니다." << endl;
    }
    return 0;
}

void ft_3()
{
    int i;

    i = 1;
    while (i <= 100)
    {
        if (i % 3 == 0)
        {
            cout << i << " ";
        }
        i++;
    }
    cout << endl;
}

void ft_sqrt()
{
    int i;
    
    for (i = 1; i <= 10; i++)
    {
        cout << i << "의 제곱은 " << i * i << "입니다." << endl;
    }
}

//1~100까지 소수 출력

void ft_prime()
{
    int i;
    int j;
    int cnt;

    for(i = 2; i <= 100; i++)
    {
        cnt = 0;
        for(j = 2; j <= i; j++)
        {
            if(i % j == 0)
            {
                cnt++;
            }
        }
        if(cnt == 1)
        {
            cout << i << " ";
        }
    }
    cout << endl;
}