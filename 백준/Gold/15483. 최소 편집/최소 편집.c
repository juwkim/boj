#include <stdio.h>
#include <string.h>
#define MAX_LEN 1001

char A[MAX_LEN], B[MAX_LEN];
short p[2][MAX_LEN];
char current;
short lenA, lenB;
short min(short x, short y, short z) {
    short m = (x < y) ? x : y;
    return (m < z) ? m : z;
}

int main() {
    scanf("%s%s", A, B);
    lenA = strlen(A);
    lenB = strlen(B);
    for (short j = 0; j <= lenB; j++) {
        p[0][j] = j;
    }

    for (short i = 0; i < lenA; i++) {
        current = (current + 1) % 2;
        char next = (current + 1) % 2;
        p[current][0] = i + 1;
        for (short j = 0; j < lenB; j++)
            p[current][j + 1] = (A[i] == B[j]) ? p[next][j] : 1 + min(p[current][j], p[next][j], p[next][j + 1]);
    }
    printf("%d\n", p[current][lenB]);
    return 0;
}
