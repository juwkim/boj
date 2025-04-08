from math import gcd

N, M, K = map(int, input().split())
p = [(x, y) for x in range(N + 1) for y in range(M + 1)]
ans = 0
for i in range(len(p) - 1):
    x1, y1 = p[i]
    for j in range(i + 1, len(p)):
        x2, y2 = p[j]
        d1, d2 = x1 - x2, y1 - y2
        if gcd(d1, d2) == K - 1:
            ans += 1
print(ans)