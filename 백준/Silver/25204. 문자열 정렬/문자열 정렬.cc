#include <bits/stdc++.h>

using namespace std;

int comp(string& a, string &b)
{
	int idx = 0;
	int size = min(a.size(), b.size());
	
	while (idx < size && a[idx] == b[idx])
		++idx;
	
	if (idx == a.size())
		return 1;
	else if (idx == b.size())
		return 0;
	
	if (a[idx] == '-')
		return 0;
	else if (b[idx] == '-')
		return 1;
	
	if (tolower(a[idx]) == tolower(b[idx]))
		return islower(b[idx]);
	return tolower(a[idx]) < tolower(b[idx]);
}

int main(void)
{
	ios::sync_with_stdio(0);cin.tie(0);
	int T; cin >> T;
	while (T--)
	{
		int N; cin >> N;
		vector<string> A;
		while (N--)
		{
			string s; cin >> s;
			A.push_back(s);
		}
		sort(A.begin(), A.end(), comp);
		for (auto s: A)
			cout << s << '\n';
	}
	return 0;
}