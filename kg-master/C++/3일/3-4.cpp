#include <string>
#include <iostream>

using namespace std;

template <class T1>
class Pair{
    private:
        T1 first;
    public:
        Pair(const T1& f): first(f){}

        T1 getFirst() const {return first;}
};

int main(){
    Pair<int>pair1(10);
    cout << "FIRST : " << pair1.getFirst()<<endl;

    Pair<double>pair2(3.14);
    cout << "first " << pair2.getFirst()<<endl;
    return 0;
}