#include <stdio.h>

#define MAX(a,b) ((a)<(b)?(b):(a))
#define MIN(a,b) ((a)>(b)?(b):(a))

	int
main( void )
{
	int g[100][100];
	int G[100][100];
	int c[101][100*100];
	int m[101];
	int n, k, i, j, s, t, M, u, v;

	for(i=0;i<101;i++) m[i]=0;

	scanf("%d %d",&n,&k);

	for(i=0;i<n;i++) for(j=0;j<n;j++){
		scanf("%d",&t);
		g[i][j] = t;
		c[t][m[t]++] = i*100+j;
	}

	for(s=0;s<=g[0][0];s++) for(t=0;t<m[s];t++){
		i = c[s][t] / 100;
		j = c[s][t] % 100;
		G[i][j] = -1;
	}

	M = s = G[0][0] = g[0][0];
	s++;

	for(;s<101;s++) for(t=0;t<m[s];t++){
		i = c[s][t] / 100;
		j = c[s][t] % 100;
		v = -1;
		for(u=MAX(i-k,0);u<MIN(i+k+1,n);u++)if(g[u][j]<s && v<G[u][j])v=G[u][j];
		for(u=MAX(j-k,0);u<MIN(j+k+1,n);u++)if(g[i][u]<s && v<G[i][u])v=G[i][u];
		if( v < 0 ) G[i][j] = -1;
		else G[i][j] = g[i][j]+v;
		if(G[i][j]>M) M=G[i][j];
	}

	printf("%d\n",M);
	return 0;
}
