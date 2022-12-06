#include <stdio.h>
int obs[200][200];
int done[200];

int main(){
   int P,T,i,j=0,k,cnt=0;
   scanf("%d%d",&P,&T);
   while (2 == scanf("%d%d",&i,&j)) {
      obs[i][j] = 1;
   }
   for (i=1;i<=P;i++) {
      if (done[i]) continue;
      cnt++;
      for (j=i;j<=P;j++) {
         for (k=1;k<=T && obs[i][k]==obs[j][k];k++);
         if (k > T) done[j] = 1;
      }
   }
   printf("%d\n",cnt);
}