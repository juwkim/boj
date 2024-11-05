#include <stdio.h>
#include <string.h>
#define MAX_LEN 1001

char A[MAX_LEN], B[MAX_LEN];
short p[2][MAX_LEN];
short lenA, lenB;

short min(short x, short y, short z) {
    return (x < y) ? ((x < z) ? x : z) : ((y < z) ? y : z);
}

int main() {
    scanf("%s %s", A, B);
    lenA = strlen(A);
    lenB = strlen(B);
    for (short j = 0; j <= lenB; j++)
        p[0][j] = j;
    for (short i = 0, cur = 1, nxt = 0; i < lenA; i++, cur ^= 1, nxt ^= 1) {
        p[cur][0] = i + 1;
        for (short j = 0; j < lenB; j++)
            p[cur][j + 1] = (A[i] == B[j]) ? p[nxt][j] : 1 + min(p[cur][j], p[nxt][j], p[nxt][j + 1]);
    }
    printf("%d\n", p[lenA & 1][lenB]);
    return 0;
}
