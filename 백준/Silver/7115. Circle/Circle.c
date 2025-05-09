#include <stdio.h>
#include <math.h>

int dist2(int x, int y) {
    return x * x + y * y;
}

int main() {
    int k, r; scanf("%d %d", &k, &r);
    int x1 = 0;
    int y1 = (r - 1) / k;
    int x2 = (int)(r / (k * sqrt(2)));
    int y2 = x2;
    double p = (double)(r) / k;
    p *= p;
    int cnt = 4;
    while (x1 != x2 || y1 != y2) {
        cnt += 8;
        if (p > dist2(x1 + 1, y1))
            x1 += 1;
        else if (dist2(x1, y1 - 1) < p && p < dist2(x1 + 1, y1))
            y1 -= 1;
        else {
            x1 += 1;
            y1 -= 1;
        }
    }
    printf("%d", cnt);
    return 0;
}