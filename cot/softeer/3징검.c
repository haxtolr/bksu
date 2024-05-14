#include <stdio.h>

void ft_check(int arr[], int n);

int main(void)
{
    int n;
    scanf("%d\n", &n);

    int arr[n];
    for (int i = 0; i < n; i++)
        {
            scanf("%d", &arr[i]);
        }

    ft_check(arr, n);

    return 0;
}

void ft_check(int arr[], int n)
{
    int lis[n];
    int result;

    for (int i = 0; i < n; i++)
        lis[i] = 1;
        
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if(arr[i] > arr[j] && lis[i] < lis[j] + 1)
                lis[i] = lis[i] + 1;
        }
    }
    result = 0;
    for (int i = 0; i < n; i++)
    {
        if (lis[i] > result)
            result = lis[i];
    }
    printf("%d", result);
}

// 9
// 2 1 7 8 11 3 4 5 6

// 5
// 9 2 1 3 8