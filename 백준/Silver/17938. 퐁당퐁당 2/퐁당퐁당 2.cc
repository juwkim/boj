#include <iostream>
using namespace std;
int main()
{
    int n, pos, t;
    cin >> n >> pos >> t;
    pos--;
    int h1 = pos * 2, h2 = pos * 2 + 1;
    int hands = 1, ud = 1, st = 0, mod = 2 * n;
    for (int i = 1; i < t; ++i)
    {
        st = (st + hands) % mod;
        if (ud) {
            if (hands == mod) {
                hands--;
                ud = !ud;
            } else hands++;		
        } else {
            if (hands == 1) {
                hands++;
                ud = !ud;
            } else hands--;
        }
    }
    for (int j = 0; j < hands; ++j)
    {
        int cur = (j + st) % mod;
        if (cur == h1 || cur == h2)
        {
            cout << "Dehet YeonJwaJe ^~^";
            return 0;
        }
    }
    cout << "Hing...NoJam";
}