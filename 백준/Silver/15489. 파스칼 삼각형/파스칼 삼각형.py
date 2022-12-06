from math import comb
R, C, W = map(int, input().split())
ans = 0
for n in range(R-1, R-1+W):
    for r in range(C - 1, C + n - (R - 1)):
        ans += comb(n, r)
print(ans)