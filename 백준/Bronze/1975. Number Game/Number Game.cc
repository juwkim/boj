# include <stdio.h>

int main() {
    int M, N, count, i, j, t;
    scanf("%d", &M);
    for (i = 0; i < M; i++) {
        scanf("%d", &N);
        count = 0;
        for (j = 2; j <= N; j++) {
            t = N;
            while (t % j == 0) {
                t /= j;
                count += 1;
            }
            if (t == 0) count += 1;
        }
        printf("%d\n", count);
    }
return 0;
}