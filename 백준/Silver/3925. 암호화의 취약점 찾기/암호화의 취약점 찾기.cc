#include <cstdio>
#define	rep(i,n) for(int i=0;i<n;i++)
#define	bit(a,i) (((a)>>(i))&1)

using namespace std;
int main(){
	int T; scanf("%d",&T);
	while (T--)
    {
		int N[9]; rep(i,9) scanf("%x", N + i);
		int ans = 0;
		rep(i,32)
        {
			int sum = 0;
			rep(j,8) sum += N[j]^ans;
			if (bit(sum, i) != bit(N[8]^ans, i))
                ans |= 1 << i;
		}
		printf("%x\n", ans);
	}
	return 0;
}