#include <stdio.h>
#include <string.h>

int main() {
    size_t n = 0;
    size_t m = 0;

    scanf("%ld %ld", &n, &m);

    printf("%ld", (n+m)*(n-m));
}