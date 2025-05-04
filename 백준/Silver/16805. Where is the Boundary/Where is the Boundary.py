n, m = map(int, input().split())
E = [0] * (n + 1)
for _ in range(m):
    for i, c in enumerate(input(), 1):
        E[i] += c == 'E'
for i in range(1, n):
    E[i + 1] += E[i]
idx = min((2 * E[i] - i * m, i) for i in range(n + 1))[1]
print(idx, idx + 1)