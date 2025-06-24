#include <stdio.h>
#include <string.h>

typedef struct { int a, b; } Pair;

int min(int x, int y) { return x < y ? x : y; }
int max(int x, int y) { return x > y ? x : y; }

int is_pair_in(Pair p[], int len, int x, int y) {
    int a = min(x, y), b = max(x, y);
    for (int i = 0; i < len; ++i) {
        if (p[i].a == a && p[i].b == b)
            return 1;
    }
    return 0;
}

int main() {
    int T;
    char num[32];
    scanf("%d", &T);
    while (T--) {
        scanf("%s", num);
        int len = strlen(num);
        Pair p[32];
        for (int i = 0; i < len - 1; ++i) {
            int a = num[i] - '0', b = num[i + 1] - '0';
            p[i].a = min(a, b);
            p[i].b = max(a, b);
        }
        int n[26] = {0};

        for (int i = 0; i < len - 1; ++i) {
            int a = p[i].a, b = p[i].b;
            if ((a == 1 && b == 2) || (a == 1 && b == 3) || (a == 2 && b == 3))
                n[0] = 1;
            else if ((a == 4 && b == 5) || (a == 4 && b == 6) || (a == 5 && b == 6))
                n[1] = 1;
            else if ((a == 7 && b == 8) || (a == 7 && b == 9) || (a == 8 && b == 9))
                n[2] = 1;
            else if ((a == 1 && b == 4) || (a == 1 && b == 7) || (a == 4 && b == 7))
                n[3] = 1;
            else if ((a == 0 && b == 2) || (a == 2 && b == 5) || (a == 2 && b == 8) || (a == 0 && b == 5) || (a == 5 && b == 8) || (a == 0 && b == 8))
                n[4] = 1;
            else if ((a == 3 && b == 6) || (a == 3 && b == 9) || (a == 6 && b == 9))
                n[5] = 1;
            else if (a == 2 && b == 6)
                n[6] = 1;
            else if ((a == 1 && b == 5) || (a == 1 && b == 9) || (a == 5 && b == 9))
                n[7] = 1;
            else if (a == 4 && b == 8)
                n[8] = 1;
            else if (a == 0 && b == 7)
                n[9] = 1;
            else if (a == 2 && b == 4)
                n[10] = 1;
            else if ((a == 3 && b == 5) || (a == 3 && b == 7) || (a == 5 && b == 7))
                n[11] = 1;
            else if (a == 6 && b == 8)
                n[12] = 1;
            else if (a == 0 && b == 9)
                n[13] = 1;
            else if (a == 1 && b == 8)
                n[14] = 1;
            else if (a == 0 && b == 4)
                n[15] = 1;
            else if (a == 2 && b == 9)
                n[16] = 1;
            else if (a == 2 && b == 7)
                n[17] = 1;
            else if (a == 3 && b == 8)
                n[18] = 1;
            else if (a == 0 && b == 6)
                n[19] = 1;
            else if (a == 1 && b == 6)
                n[20] = 1;
            else if (a == 4 && b == 9)
                n[21] = 1;
            else if (a == 3 && b == 4)
                n[22] = 1;
            else if (a == 6 && b == 7)
                n[23] = 1;
            else if (a == 0 && b == 1)
                n[24] = 1;
            else if (a == 0 && b == 3)
                n[25] = 1;
        }
        int cnt = 0;
        for (int i = 0; i < 26; ++i) cnt += n[i];
        int cond1 = is_pair_in(p, len - 1, 2, 5);
        int cond2 = is_pair_in(p, len - 1, 0, 8);
        int cond3 = !is_pair_in(p, len - 1, 2, 8);
        int cond4 = !is_pair_in(p, len - 1, 0, 2);
        int cond5 = !is_pair_in(p, len - 1, 5, 8);
        int cond6 = !is_pair_in(p, len - 1, 0, 5);
        if (cond1 && cond2 && cond3 && cond4 && cond5 && cond6)
            cnt += 1;
        if (cnt <= 3)
            printf("EXCELLENT\n");
        else if (cnt == 4)
            printf("GOOD\n");
        else
            printf("BAD\n");
    }
    return 0;
}