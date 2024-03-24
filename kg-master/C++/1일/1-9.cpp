#include <iostream>

using namespace std;

int main() 
{
  int i;
  int n;

  i = 0;
  while (i < 5) 
  {
    cout << "숫자 : ";
    cin >> n;
    if (n < 0) 
    {
      cout << "음수" << endl;
      continue;
    }
    cout << "입력한 숫자: " << n << endl;
    i++;
  }
  return 0;
}