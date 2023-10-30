#include <stdio.h>
#include <stdlib.h>

char jane[200], john[200];
int janei, johni;

int main()
{
   int i, j;
   gets(jane); gets(john);
   for (j=0;j<1000 && strlen(jane)&&strlen(john);j++){
      if (jane[janei] == john[johni]) {
         if (random()/141%2 == 0) { /* jane wins */
            printf("Snap! for Jane: ");
            for (i=strlen(jane);i>janei;i--) jane[i+johni+1] = jane[i];
            strncpy(jane+janei+1,john,johni+1);
            strcpy(john,john+johni+1);
            janei = janei + johni + 2;
            johni = 0;
            for (i=janei-1;i>=0;i--) printf("%c",jane[i]);
            printf("\n");
         }else{  /* john wins */ 
            printf("Snap! for John: ");
            for (i=strlen(john);i>johni;i--) john[i+janei+1] = john[i];
            strncpy(john+johni+1,jane,janei+1);
            strcpy(jane,jane+janei+1);
            johni = johni + janei + 2;
            janei = 0;
            for (i=johni-1;i>=0;i--) printf("%c",john[i]);
            printf("\n");
         }
      }else{
         janei++; johni++;
      }
      if (!jane[janei]) janei = 0;
      if (!john[johni]) johni = 0;
   }
   if (!strlen(jane)) printf("John wins.\n");
   else if (!strlen(john)) printf("Jane wins.\n");
   else printf("No winner after %d turns\n",j);
}