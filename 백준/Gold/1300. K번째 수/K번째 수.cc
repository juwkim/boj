#include<iostream>
#include<algorithm>
using namespace std;

long long N, K;
long long l, r, mid;
long long cnt;

long long count(long long x)
{
	long long sum = 0;
	for (int i = 1; i <= N; i++) 
        sum += min(x / i, N);
    
	return sum;
}

int main()
{
	cin >> N >> K;

	l = 1;
	r = N * N;

	while (l <= r)
	{
		mid = (l + r) / 2;

		cnt = count(mid);

		if (cnt >= K) r = mid - 1;
		else l = mid + 1;
	}
    
	cout << l;
}