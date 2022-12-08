from collections import Counter
g = lambda: map(int, input().split())
input()
ans, cnt = 0, Counter(g())
for num in g():
    if cnt[num]: cnt[num] -= 1
    else: ans += 1
print(ans)