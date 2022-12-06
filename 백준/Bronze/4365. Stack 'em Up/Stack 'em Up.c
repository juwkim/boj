#include <stdio.h>

int d[101][53];
int deck[53], newdeck[53];
char *suit[] = {"Clubs", "Diamonds", "Hearts", "Spades"};
char *value[] = {"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"};
int i,j,k,deal,deals;

int main() {
   scanf("%d", &deals);
   for (i=1; i<=deals; i++)
       for (j=1;j<=52;j++)
           scanf("%d",&d[i][j]);
   for (i=1;i<=52;i++)
       deck[i] = i;
   while (1 == scanf("%d",&deal)) {
      for (i=1;i<=52;i++) newdeck[i] = deck[d[deal][i]];
      for (i=1;i<=52;i++) deck[i] = newdeck[i];
      for (i=1;i<=52;i++) {
         printf("%s of %s\n",value[(deck[i]-1)%13],suit[(deck[i]-1)/13]);
      }
      printf("\n");
   }
}