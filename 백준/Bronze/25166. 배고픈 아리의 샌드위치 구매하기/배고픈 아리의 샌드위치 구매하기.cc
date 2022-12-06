#include <bits/stdc++.h>
using namespace std;

#define FASTIO cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define ROF(i,a,b) for(int i=(a);i>=(b);i--)
#define ll long long int
#define pii pair<int, int>
#define PQ priority_queue
#define LEN(v) int(v.size())
#define ALL(v) v.begin(),v.end()
#define INF 2e9
#define LINF 1e18

int main() {
	FASTIO;
	int S, M;
	cin >> S >> M;
	if (S <= 1023) {
		cout << "No thanks";
	}
	else {
		S -= 1023;
		bool flag = true;
		FOR(i, 0, 10) {
			bool f1 = S & (1 << i);
			bool f2 = M & (1 << i);
			if (f1 && !f2) {
				flag = false;
			}
		}
		cout << (flag ? "Thanks" : "Impossible");
	}

	return 0;
}