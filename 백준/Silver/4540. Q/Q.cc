#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main (void) {

   int datasets, i;
   char *queueA[20];
   char *queueB[20];
   int moved[20];
   int nextslot;

   scanf("%d",&datasets);

   for (i=0; i<datasets; i++) {

      int m, n, j, source, target;

      /* read in data set parameters */
      scanf("%d %d", &m, &n);

      /* read in the starting queue */
      for (j=0; j<m; j++) {
         char temp[10];
         scanf ("%s", temp);
         queueA[j]=strdup(temp);
         queueB[j]=NULL;
         moved[j]=0;
      }

      /* process the moves */
      for (j=0; j<n; j++) {
         scanf("%d %d", &source, &target);
         queueB[target-1]=queueA[source-1];
         moved[source-1]=1;
      }

      /* drop in all the unmoved items */
      nextslot=0;
      for (j=0; j<m; j++) {
         if (!moved[j]) {
             while (queueB[nextslot] != NULL) nextslot++;
             queueB[nextslot]=queueA[j];
             nextslot++;
         }
      }

      /* display the resulting queue */
      for (j=0; j<m; j++) {
         printf("%s ",queueB[j]);
      }
      printf("\n");

   }

}