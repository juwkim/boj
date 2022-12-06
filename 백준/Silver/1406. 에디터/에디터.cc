#include <bits/stdc++.h>

using namespace std;
int main() {
	cin.tie(nullptr)->ios_base::sync_with_stdio(false);
	string A; cin >> A;
	list<int> lt;
	for (char c : A)
		lt.push_back(c);

	auto cur = lt.end();
	int M; cin >> M;
	while (M--)
	{
		char cmd; cin >> cmd;
		switch (cmd)
		{
		case 'L':
			if (cur != lt.begin())
				--cur;
			break;
		case 'D':
			if (cur != lt.end())
				++cur;
			break;
		case 'B':
			if (cur != lt.begin())
				cur = lt.erase(--cur);
			break;
		default:
			char c; cin >> c;
			cur = ++lt.insert(cur, c);
			break;
		}
	}
	for (char c : lt)
		cout << c;
	return 0;
}