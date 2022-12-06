#include <bits/stdc++.h>

using namespace std;
int main() {
	cin.tie(nullptr)->ios_base::sync_with_stdio(false);

	list<int> lt;
	int M; cin >> M;
	while (M--)
	{
		string A; cin >> A;
		lt.clear();
		auto cur = lt.end();
		for (char c : A)
		{
			switch (c)
			{
			case '<':
				if (cur != lt.begin())
					--cur;
				break;
			case '>':
				if (cur != lt.end())
					++cur;
				break;
			case '-':
				if (cur != lt.begin())
					cur = lt.erase(--cur);
				break;
			default:
				cur = ++lt.insert(cur, c);
				break;
			}
		}
		for (char c : lt)
			cout << c;
		cout << '\n';
	}
	return 0;
}