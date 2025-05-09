#include <stdio.h>
#include <math.h>

int main() {
    long long x, y, r;
    while (1) {
        scanf("%d %d %d", &x, &y, &r);
        if (x == 0) break;
        long long count = r;
        for (long long i = 0; i < r; ++i)
            count += (long long)sqrt(r * r - i * i - 1);
        printf("%lld\n", count * 4);
    }
    return 0;
}