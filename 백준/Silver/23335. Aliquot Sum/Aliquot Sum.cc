#include <bits/stdc++.h>

using namespace std;
int main()
{
    cin.tie(nullptr)->sync_with_stdio(false);
    int T; cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int num; cin >> num;
        int Sum = -num;
        for (int a = 1; a <= (int)sqrt(num); ++a)
        {
            if (num % a == 0)
            {
                int b = num / a;
                Sum += a;
                if (a != b)
                    Sum += b;
            }
        }
        if (Sum > num)
            cout << "abundant\n";
        else if (Sum < num)
            cout << "deficient\n";
        else
            cout << "perfect\n";
    }

    return 0;
}