#include "grader.h"
#include "memory.h"

void play() {
   char a;
   int buf[25] = {0, };
   for (int i=1; i<=50; ++i) {
      a = faceup(i);
      int idx = a - 'A';
      if (buf[idx])
      {
          faceup(buf[idx]);
          faceup(i);
      }
      else {
          buf[idx] = i;
      }
   }
}