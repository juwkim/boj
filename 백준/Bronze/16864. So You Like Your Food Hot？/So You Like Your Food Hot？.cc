#include <iostream>

using namespace std;

int main() {
  int d,c,total,pizza,pita;
  char dot;
  bool flag=true;

  cin >> d >> dot >> c;
  total = d * 100 + c;

  cin >> d >> dot >> c;
  pizza = d * 100 + c;

  cin >> d >> dot >> c;
  pita = d * 100 + c;

  for (int i=0;total-i*pizza>=0;i++)
    if ((total-i*pizza)%pita == 0) {
      cout << i << ' ' << (total-i*pizza)/pita << endl;
      flag = false;
    }

  if (flag)
    cout << "none" << endl;

  return 0;
}