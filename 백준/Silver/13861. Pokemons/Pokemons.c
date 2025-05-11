#include <stdio.h>

int n;
double money, price, min_price, ratio, max_ratio = -1e18;
int main() {
    scanf("%lf %d %lf", &money, &n, &min_price);
    for (int i = 1; i < n; ++i) {
        scanf("%lf", &price);
        if (price > max_ratio * min_price) max_ratio = price / min_price;
        if (price < min_price) min_price = price;
    }
    printf("%.2f\n", (max_ratio - 1) * money + 1e-8);
    return 0;
}