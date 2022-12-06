#include <stdio.h>

int n,p;
char prop[81], bestprop[81];
double price,bestprice;
int r,bestr;

main(){
   int i,j,k;
   for (i=1;;i++){
      scanf("%d%d\n",&n,&p);
      if (n == 0) break;
      bestr = -1;
      for (j=0;j<n;j++){
         gets(prop);  /* junk */
      }
      for (k=0;k<p;k++){
         gets(prop);
         scanf("%lf%d\n",&price,&r);
         if (r > bestr || (r == bestr && price < bestprice)) {
            bestr = r;
            bestprice = price;
            strcpy(bestprop,prop);
         }
         for (j=0;j<r;j++){
            gets(prop);  /* junk */
         }
      }
      if (i != 1) printf("\n");
      printf("RFP #%d\n%s\n",i,bestprop);
   }
}