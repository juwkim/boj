# include <stdio.h>
int main() {
	int n, weight, lmax_weight = 0, diff = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &weight);
		if (weight > lmax_weight) lmax_weight = weight;
		if (lmax_weight - weight > diff) diff = lmax_weight - weight;
	}
	printf("%d\n", diff);
    return 0;
}