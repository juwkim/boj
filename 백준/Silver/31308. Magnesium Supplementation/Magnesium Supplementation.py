from math import isqrt

n, k, p = map(int, input().split())
ans = []
for i in range(1, min(k, isqrt(n)) + 1):
    j, r = divmod(n, i)
    if r:
        continue
    if j <= p:
        ans.append(i)
    if i != j and i <= p and j <= k:
        ans.append(j)
print(len(ans))
for l in sorted(ans):
    print(l)