#include <bits/stdc++.h>

using namespace std;

bool adj[26][26];
int component[26];

int N, M, K;

void dfs(int _class, int compId)
{
	if (component[_class] != 0)
		return;
	component[_class] = compId;
	
	for (int nc = 0; nc < K; nc++)
	{
		if (adj[_class][nc])
		{
			dfs(nc, compId);
		}
	}
}

int main()
{
	cin >> N >> M >> K;
	
	vector<string> rows(N);
	for (int r = 0; r < N; r++)
	{
		cin >> rows[r];
	}
	
	for (int c = 0; c < M; c++)
	{
		int cl0 = rows[0][c] - 'A';
		for (int r = 0; r < N; r++)
		{
			int cl1 = rows[r][c] - 'A';
			adj[cl0][cl1] = true;
			adj[cl1][cl0] = true;
		}
	}
	
	int numComponents = 0;
	for (int i = 0; i < K; i++)
	{
		if (component[i] == 0)
		{
			numComponents++;
			dfs(i, numComponents);
		}
	}
	
	cout << numComponents << endl;
}
