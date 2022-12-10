g = lambda: [*map(int, input().split())]

from collections import Counter
N = int(input())
cnt = Counter(g())
ans, left = 0, 0
for key, val in sorted(cnt.items()):
    if val <= left:
        left -= val
        ans += left == 0
    else:
        ans += left != 0
        q, r = divmod(val - left, key)
        left = (key - r) % key
        ans += q
ans += left != 0
print(ans)