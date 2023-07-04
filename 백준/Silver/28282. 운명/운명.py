g = lambda: [*map(int, input().split())]

X, K = g()
left, right = [0] * (K + 1), [0] * (K + 1)
colors = g()
for i in range(X):
    left[colors[i]] += 1
for i in range(X, 2 * X):
    right[colors[i]] += 1

ans = 0
for i in range(1, K + 1):
    ans += left[i] * (X - right[i])
print(ans)