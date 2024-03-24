#include <stdio.h>


float ft_cal(int grade[], int f, int d);

int main(void)
{
    int n;
    int k;
    int grade[n];
    int sect[k][2];

    scanf("%d %d", &n, &k);

    for (int i = 0; i<n; i++)
    {    
        scanf("%d", &grade[i]);
    }
    for (int i = 0; i<k; i++)
    {
        scanf("%d %d", &sect[i][0], &sect[i][1]);
    }
    for (int i = 0; i <k; i++)
    {
        printf("%f\n", ft_cal(&grade[n], sect[i][0], sect[i][1]));
    }
    
    
   return 0;
}

float ft_cal(int grade[], int f, int d)
{
    int num;
    float result;
    int sum;
    
    num = d - f + 1;
    f--;
    sum = 0;
    while (f != d)
    {
        sum = grade[f] + sum;
        f++;
    }
    return result/sum;
}


