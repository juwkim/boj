#include <cstdio>

const int MAXX = 1 << 20;

char buf[MAXX];
int p;

inline char _read_char()
{
	if (p == MAXX)
	{
		fread(buf, 1, MAXX, stdin);
		p = 0;
	}

	return buf[p++];
}

inline void readInt(int &x)
{
	int tmp;

	x = _read_char() & 0b1111;

	while ((tmp = _read_char()) != '\n')
	{
		x = x * 10 + (tmp & 0b1111);
	}
}

int main()
{
	// Declaration
	long long r = 0;
	int n, t;


	// Input
	readInt(n);
	printf("%d\n", n);  // Output
	while (n--)
	{
		readInt(t);
		r += t;  // Solve
	}


	// Output
	printf("%lld", r);
}