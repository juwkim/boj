#include <cstdio>

int main() {
    int n;
    long long S = 0;
    scanf("%d", &n);
    for (int x, i = 0; i < n; ++i) {
        scanf("%d", &x);
        S += x;
    }
    int m = S - (long long)n * (n - 1) / 2LL;
    printf("%d\n", m);
    return 0;
}