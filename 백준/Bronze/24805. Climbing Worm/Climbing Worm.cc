#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int cnt = 0;
	int cur = 0;
	int sU, sD, H; cin >> sU >> sD >> H;

	while (1) {
		cur += sU, cnt++;
		if (cur >= H) break;
		cur -= sD;
	}

	cout << cnt;
}