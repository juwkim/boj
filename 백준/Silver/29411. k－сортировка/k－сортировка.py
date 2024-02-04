
import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
a = g()
b = sorted(a)
idx = {num: i for i, num in enumerate(a)}
ans = "YES"
for i in range(n - 1):
    if a[i] == b[i]:
        continue
    if (a[i] - b[i]) % k:
        ans = "NO"
        break 
    j = idx[b[i]]
    idx[a[i]], idx[b[i]] = j, i
    a[i], a[j] = a[j], a[i]
print(ans)