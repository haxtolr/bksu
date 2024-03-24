#include <iostream>
#include <string>

using namespace std;

class calc 
{
public:
    int ft_sum(int a, int b);
    int ft_sub(int a, int b);
    int ft_div(int a, int b);
    int ft_mul(int a, int b);
    int ft_mean(int a, int b);
    int ft_mean(int a, int b, int c);
};

int calc::ft_sum(int a, int b) 
{
    return (a + b);
}

int calc::ft_sub(int a, int b) {
    return (a - b);
}

int calc::ft_div(int a, int b) 
{
    return (a / b);
}

int calc::ft_mul(int a, int b) 
{
    return (a * b);
}

int calc::ft_mean(int a, int b) 
{
    return(ft_div(ft_sum(a, b), 2));
}

int calc::ft_mean(int a, int b, int c) 
{
    return((a + b + c) / 3);
}

int main() {
    int num1;
    int num2;
    char lx[100];
    char c;
    int i;
    int t;
    calc cal;

    i = 0;
    num1 = 0;
    num2 = 0;

    cout << "식 : ";
    cin.getline(lx, 100);

    while (lx[i] != '+' && lx[i] != '-' && lx[i] != '*' && lx[i] != '/') 
    {
        i++;
    }
    c = lx[i];
    i = 0;
    while (lx[i] != '+' && lx[i] != '-' && lx[i] != '*' && lx[i] != '/') 
    {
        num1 = num1 * 10 + (lx[i] - '0');
        i++;
    }
    i++;
    while (lx[i] != '\0') 
    {
        num2 = num2 * 10 + (lx[i] - '0');
        i++;
    }

    if (c == '+')
        cout << "더하기 : " << cal.ft_sum(num1, num2) << endl;
    else if (c == '-')
        cout << "빼기 : " << cal.ft_sub(num1, num2) << endl;
    else if (c == '/')
        cout << "나누기 : " << cal.ft_div(num1, num2) << endl;
    else if (c == '*')
        cout << "곱하기 : " << cal.ft_mul(num1, num2) << endl;

    return 0;
}