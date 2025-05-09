#include <stdio.h>

int dist2(int x, int y) {
    return x * x + y * y;
}

int main() {
    int k, r; scanf("%d %d", &k, &r);
    int x = 0;
    int y = (r - 1) / k;
    double p = (double)(r) / k;
    p *= p;
    int cnt = 4;
    while (y > x) {
        cnt += 8;
        if (p > dist2(x + 1, y))
            x += 1;
        else if (dist2(x, y - 1) < p && p < dist2(x + 1, y))
            y -= 1;
        else {
            x += 1;
            y -= 1;
        }
    }
    printf("%d", cnt);
    return 0;
}