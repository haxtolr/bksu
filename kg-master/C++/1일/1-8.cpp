#include <string>
#include <iostream>

using namespace std;


void ft_7();
void ft_yn();

int main()
{
    int a;

    cout << "mission : ";
    cin >> a;

    if (a == 1)
        ft_7();
    else if (a==2)
        ft_yn();
    else
        return 0;
    return 0;
}

void ft_7()
{
    int i = 1;
    
    do {
        cout << 7 * i << endl;
     i++;
    } while (7 * i <= 100);
    
    return ;   
}

void ft_yn()
{
    char c;

    do{
        cout << c << endl;
        cin >> c;
    } while (c != 'n');
    
    return ;
}