#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    if (n >= 8)
        cout << n - 7;
    else
        cout << m + 7;
}