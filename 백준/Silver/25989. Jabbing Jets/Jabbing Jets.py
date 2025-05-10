import math

n, e, *rs = map(int, open(0).read().split())
e /= 2
ans = 0
for r in rs:
    if e > r:
        ans += 1
    else:
        ans += int(math.pi / math.asin(e / (r + 1e-6)))
print(ans)