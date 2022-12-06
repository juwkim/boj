#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1005;
const int M = 12;

int n, m;
int a[N], b[N];

void doit()
{
	scanf("%d%d", &m, &n);

	for (int i = 1; i <= n + 1; ++i)
	{
		a[i] = 0;
		for (int j = 0; j < m; ++j)
		{
			int x;
			scanf("%d", &x);
			a[i] += x << j;
		}
		if (i <= n)
			scanf("%d", &b[i]);
	}
	b[n + 1] = 0;

	int max_pt = -(1 << 28), min_pt = 1 << 28;
	for (int i = 1; i <= n; ++i)
	{
		int j = n + 1;
		int pt = __builtin_popcount(a[i] & a[j]) * (b[i] - b[j]);
		// printf("%d %d\n", i, pt);
		max_pt = max(max_pt, pt);
		min_pt = min(min_pt, pt);
	}
	printf("%d\n\n", max_pt - min_pt);
}

int main()
{
	int K;
	scanf("%d", &K);
	for (int _ = 1; _ <= K; ++_)
	{
		printf("Data Set %d:\n", _);
		doit();
	}

	return 0;
}