#include <iostream>
#include <string>

using namespace std;

struct Human {
    int age;
    int height;
    string name;
};

void setHuman(Human *ptr, int a, int h, string n)
{
    ptr->age = a;
    ptr->height = h;
    ptr->name = n;
}

int main()
{
    Human h;

    setHuman(&h, 10, 20, "asdf");
    cout << h.age <<endl;
    cout << h.height << endl;
    cout << h.name << endl;
}