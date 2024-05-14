#include <iostream>
#include <string>

using namespace std;

struct student{
    string name;
    int age;
    int num;
    string gen;
};

void get_st(student *st, string na, int a, int n, string g)
{
    st->name = na;
    st->age = a;
    st->num = n;
    st->gen = g;

    cout << "이름 : " << st->name << endl;
    cout << "나이 : " << st->age << endl;
    cout << "학번 : " << st->num << endl;
    cout << "성별 : " << st->gen << endl;
}

int main()
{
    student st;

    get_st(&st, "홍", 12, 30102201, "남");
    
}