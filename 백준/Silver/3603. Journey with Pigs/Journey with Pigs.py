g = lambda: [*map(int, input().split())]

n, t = g()
weights = g()
distances = g()
prices = g()
villages = sorted(range(n), key=lambda i: t * distances[i] - prices[i])
pigs = sorted(range(n), key=lambda i: -weights[i])
ans = [0] * n
for a, b in zip(villages, pigs):
    ans[a] = b + 1
print(*ans)