g = lambda: [*map(int, input().split())]

from collections import Counter
input()
ans = 0
cnt = Counter(g())
for num in g():
    if cnt[num]:
        cnt[num] -= 1
    else:
        ans += 1
print(ans)