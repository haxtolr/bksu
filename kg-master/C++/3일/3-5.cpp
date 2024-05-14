#include <iostream>

using namespace std;

template <typename T>
class MinMax {
public:
    MinMax(T a, T b) {
        if (a < b) {
            min = a;
            max = b;
        } else {
            min = b;
            max = a;
        }
    }
    T min;
    T max;
};

int main() {
    MinMax<int> mm(10, 20);
    cout << "최소 : " << mm.min << endl;
    cout << "최대 : " << mm.max << endl;

    return 0;
}
