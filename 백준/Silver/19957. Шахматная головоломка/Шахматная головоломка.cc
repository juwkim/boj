#include <iostream>
using namespace std;
 
int main() {
    int k1;
    char k0;
    cin >> k0 >> k1;
    int n = 8; //Вводим n, чтобы иметь возможность изменить размер доски 
    char mid = char (('a' + n) - n / 2); //Находим середину доски
    if ( k1 != 1) {
        if (k0 < mid) cout << char(k0 + 3) << k1 << "\n" << char(k0 + 1) << k1 - 1;
        else cout << char(k0 - 3) << k1 << "\n" << char(k0 - 1) << k1-1;
    }
    else {
        if (k0 < mid) cout << char(k0 + 3) << k1 << "\n" << char(k0 + 1) << k1 + 1;
        else cout << char(k0 - 3) << k1 << "\n" << char(k0 - 1) << k1 + 1;
    } 
    return 0;
}