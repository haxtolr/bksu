#include <stdlib.h>

int main() {
    system("find . -type f ! -name '*.c' ! -name '*.cpp' ! -name '*.h' ! -name 'makefile' -exec rm -f {} +");
    system("find . -name '*.dSYM' -type d -exec rm -rf {} +");
    return 0;
}