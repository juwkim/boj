#include <bits/stdc++.h>

using namespace std;
char A[13], B[13];
__int128_t mod = 1'000'000'000'000'000'000LL;
int sign = 0;

__int128_t solve(char *s) {
    int i;
    if (s[0] == '-') {
        i = 3;
        sign ^= 1;
    } else {
        i = 2;
    }
    __int128_t ret = s[i - 2] - '0';
    for (int j = i; j < i + 9; ++j)
        ret = 10 * ret + s[j] - '0';
    return ret;
}

int main() {
    int N; cin >> N;
    ios::fmtflags originalFlags = cout.flags();
    while (N--) {
        cin >> A >> B;
        __int128_t p = solve(A) * solve(B);
        if (sign) {
            cout << '-';
            sign = 0;
        }
        cout << (long long)(p / mod) << '.' << setfill('0') << setw(18) << (long long)(p % mod) << '\n';
        cout.flags(originalFlags);
    }
    return 0;
}