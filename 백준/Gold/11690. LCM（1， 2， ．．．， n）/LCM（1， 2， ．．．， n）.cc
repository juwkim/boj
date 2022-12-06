#include <bits/stdc++.h>

using namespace std;
#define MAXSIZE 100000001
bool Array[MAXSIZE];
int main() {
	cin.tie(nullptr)->sync_with_stdio(false);

	long long LCM = 1;
	long long mod = 4294967296;
	int N; cin >> N;
    
    while (LCM * 2 <= N) LCM *= 2;
    
    memset(Array, true, MAXSIZE);

	for (long long i = 3; i <= N; i = i + 2)
	{
		if (Array[i])
		{
			for (long long j = i * i; j <= N; j += i)
				Array[j] = false;

			long long num = i;
			while (num <= N)
			{
				LCM = (LCM * i) % mod;
				num *= i;
			}
		}
	}
	cout << LCM % mod << '\n';
	return 0;
}