#include <stdio.h>
#include <math.h>

int main() {
    long long x, y, r;
    while (1) {
        scanf("%d %d %d", &x, &y, &r);
        if (x == 0) break;
        long long count = 0;
        for (int i = 0; i < r; i++)
            count += (long long)sqrt(r * r - 1LL * i * i - 1) + 1;
        printf("%lld\n", count * 4);
    }
    return 0;
}