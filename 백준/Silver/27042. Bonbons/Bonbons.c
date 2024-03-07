#include <stdio.h>
main(int n){scanf("%d",&n);int i=1;while(n>i){n-=i;i*=2;}printf("%d",n*2-1);}