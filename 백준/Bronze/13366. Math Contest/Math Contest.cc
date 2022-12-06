#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T, p;
    string n;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cin >> n;
        p = - ('0' * n.size());
        for (auto x: n)
            p += x;
        if (p % 9)
            cout << "NO" << '\n';
        else
            cout << "YES" << '\n';
    }
    return 0;
}