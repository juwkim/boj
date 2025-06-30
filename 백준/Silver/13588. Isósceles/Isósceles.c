#include <stdio.h>
#include <stdlib.h>

#define MAXN 50000

int N;
int heights[MAXN + 1];
int is_possible(int h) {
    for (int center = h - 1; center <= N - h; ++center) {
        int ok = 1;
        for (int off = -h + 1; off < h; ++off) {
            if (heights[center + off] < h - abs(off)) {
                ok = 0;
                break;
            }
        }
        if (ok) return 1;
    }
    return 0;
}

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
        scanf("%d", heights + i);
    int lo = 1, hi = (N + 1) / 2;
    int max_height = heights[0];
    for (int i = 1; i < N; ++i) {
        if (heights[i] > max_height) max_height = heights[i];
    }
    if (hi > max_height) hi = max_height;
    hi += 1;
    while (hi > lo + 1) {
        int mid = (lo + hi) / 2;
        if (is_possible(mid))
            lo = mid;
        else
            hi = mid;
    }
    printf("%d\n", lo);
    return 0;
}