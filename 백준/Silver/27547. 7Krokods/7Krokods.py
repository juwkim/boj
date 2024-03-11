from collections import Counter

n, m = map(int, input().split())
cnt = Counter(input())
ans = 0
for x in range(0, m + 1):
    for y in range(0, m - x + 1):
        for z in range(0, m - x - y + 1):
            w = m - x - y - z
            d, k, o, r = cnt['d'] + x, cnt['k'] + y, cnt['o'] + z, cnt['r'] + w
            ans = max(ans, d*d + k*k + o*o + r*r + min(d, k//2, o//2, r) * 7)
print(ans)