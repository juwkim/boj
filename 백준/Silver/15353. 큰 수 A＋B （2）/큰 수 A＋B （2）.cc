#include <bits/stdc++.h>

using namespace std;
int ans[10002] = { 0, };
int main() {
	cin.tie(nullptr)->ios_base::sync_with_stdio(false);
	
	string A, B;
	cin >> A >> B;

	size_t a = A.size();
	size_t b = B.size();
	int cur = 0;
	int A_cur = a - 1, B_cur = b - 1;


	for (; (B_cur >= 0) && (A_cur >= 0); --B_cur, --A_cur, ++cur)
	{
		int num = A[A_cur] + B[B_cur] - '0' - '0';
		ans[cur] += num;
		if (ans[cur] > 9)
		{
			ans[cur + 1] = ans[cur] / 10;
			ans[cur] %= 10;
		}
	}
	for (; A_cur >= 0; --A_cur, ++cur)
	{
		int num = A[A_cur] - '0';
		ans[cur] += num;
		if (ans[cur] > 9)
		{
			ans[cur + 1] = ans[cur] / 10;
			ans[cur] %= 10;
		}
	}
	for (; B_cur >= 0; --B_cur, ++cur)
	{
		int num = B[B_cur] - '0';
		ans[cur] += num;
		if (ans[cur] > 9)
		{
			ans[cur + 1] = ans[cur] / 10;
			ans[cur] %= 10;
		}
	}
	if (ans[cur] == 0)
		--cur;
	for (; cur >= 0; --cur)
	{
		cout << ans[cur];
	}



	return 0;
}