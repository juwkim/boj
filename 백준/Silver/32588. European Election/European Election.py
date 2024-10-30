import sys
g = lambda: map(int, sys.stdin.readline().split())

n, k = g()
a = [[0] * (k + 1) for _ in range(k + 1)]
s = set(range(1, k + 1))
for _ in range(n):
    v, *p = g()
    for i in range(v - 1):
        for j in range(i + 1, v):
            a[p[i]][p[j]] += 1
    for num2 in s - set(p):
        for num1 in p:
            a[num1][num2] += 1
ans = "impossible"
for i in range(1, k + 1):
    if all(i == j or a[i][j] > a[j][i] for j in range(1, k + 1)):
        ans = i
        break
print(ans)