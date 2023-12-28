from itertools import combinations, product
g = lambda: [*map(int, input().split())]

l = g()
N = int(input())
buf = [g() for _ in range(N)]
ans = 0
for a, b in combinations(buf, 2):
    for i, j, k in product(range(2), repeat=3):
        if a[i] + b[j] <= l[k] and a[i^1] <= l[k^1] and b[j^1] <= l[k^1]:
            ans = max(ans, a[0] * a[1] + b[0] * b[1])
print(ans)