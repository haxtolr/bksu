#include <iostream>
#include <string>

using namespace std;

class employee 
{
protected:
    string name;
    int age;
public:
    employee(string name, int age) : name(name), age(age) {}
    void ft_printf() 
    {
        cout << "이름: " << name << " 나이: " << age << endl;
    }
};

class manager : public employee 
{
private:
    string dep;
public:
    manager(string name, int age, string dep) : employee(name, age), dep(dep) {}

    void ft_printf() 
    {
        cout << "이름: " << name << " 나이: " << age << " 부서: " << dep << endl;
    }
};

int main()
{
    employee emp("김밥", 1);
    emp.ft_printf();

    manager manager("호랑이", 4, "동물");
    manager.ft_printf();

    return 0;
}
