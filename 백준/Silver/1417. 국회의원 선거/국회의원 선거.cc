#include <iostream>
#include <queue>

using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	if (N == 1)
		cout << 0 << '\n';
	else
	{
		int dasom;
		cin >> dasom;

		int x;
		priority_queue<int> pq;
		for (int i = 1; i < N; ++i)
		{
			cin >> x;
			pq.push(x);
		}
		int ans = 0;
		while (true)
		{
			int tmp = pq.top();
			if (tmp >= dasom)
			{
				pq.pop();
				pq.push(--tmp);
				++dasom;
				++ans;
			}
			else
			{
				cout << ans << '\n';
				break;
			}
		}
	}
	return 0;
}