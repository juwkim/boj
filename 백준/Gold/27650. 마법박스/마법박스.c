#include <stdio.h>
#include <stdbool.h>

bool notprime[5000000 + 1];

int main()
{
	int	N;
	scanf("%d", &N);

	int prime[348513];
	int	idx = 0;
	for (int i = 2; i <= N; ++i)
	{
		if (notprime[i] == false)
		{
			prime[idx++] = i;
			for (long long j = (long long ) i * i; j <= N; j += i)
				notprime[j] = true;
		}
	}

	int	l = 0;
	int	r = idx - 1;
	int	mid;
	bool res;

    while (l <= r)
	{
        mid = l + r >> 1;
		printf("? %d\n", prime[mid]);
		fflush(stdout);
		scanf("%d", &res);
        if (res == 1)
			l = mid + 1;
        else
			r = mid - 1;
    }
	printf("! %d", prime[r + 1]);
}