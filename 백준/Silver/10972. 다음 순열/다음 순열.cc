#include <bits/stdc++.h>

using namespace std;
int N;

int main() {
	cin.tie(nullptr)->ios_base::sync_with_stdio(false);

	cin >> N;	
	vector<int> vi;
	for (int i = 0; i < N; i++)
	{
		int num; cin >> num;
		vi.push_back(num);
	}

	bool res = next_permutation(vi.begin(), vi.end());

	if (res)
	{
		for (auto num : vi)
			cout << num << " ";
	}
	else
		cout << -1;

	return 0;
}