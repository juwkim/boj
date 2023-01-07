#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#include <bits/stdc++.h>
typedef long long ll;
typedef long double ld;
using namespace std;
const int N = 1e5 + 5;
ll x, y, d1, a, b, d2;
int main() {
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    cin >> x >> y >> d1 >> a >> b >> d2;
    if(abs(x - a) + abs(y - b) > d1 + d2)
		return cout << "impossible", 0;
    if(((x + y + d1) & 1) != ((a + b + d2) & 1))
		return cout << "impossible", 0;
	if(x < a) {
		ll need = min(d2, a - x);
		d2 -= need, a -= need;
	} else {
		ll need = min(d2, x - a);
		d2 -= need, a += need;
	}
	if(y < b) {
		ll need = min(d2, b - y);
		d2 -= need, b -= need;
	} else {
		ll need = min(d2, y - b);
		d2 -= need, b += need;
	}
	if(d2 & 1)
		a++;
	cout << a << " " << b;
    return 0;
}