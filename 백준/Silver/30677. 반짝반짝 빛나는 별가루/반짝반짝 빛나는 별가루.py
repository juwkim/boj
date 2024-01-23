import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K, C, R = g()
base, s, p = g(), g(), g()
combo, skill = 0, [0] * K
ans, tired = 0, 0
prev = -1
for _ in range(N):
    l = int(input())
    if l == 0:
        combo = 0
        tired = max(0, tired - R)
    else:
        l -= 1
        tired += p[l]
        if tired > 100:
            ans = -1
            break
        ans += base[l] * (100 + combo * C) * (100 + skill[l] * s[l]) // 10000
        combo += 1
        skill[l] += 1
    prev = l
print(ans)