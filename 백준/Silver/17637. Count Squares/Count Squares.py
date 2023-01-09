def g(): return [*map(int, input().split())]

from collections import Counter

h, v = g()

nums = g()
cnt_h = Counter([nums[j] - nums[i] for i in range(h - 1) for j in range(i + 1, h)])

nums = g()
cnt_v = Counter([nums[j] - nums[i] for i in range(v - 1) for j in range(i + 1, v)])

ans = 0
for key in cnt_h:
    ans += cnt_h[key] * cnt_v[key]
print(ans)