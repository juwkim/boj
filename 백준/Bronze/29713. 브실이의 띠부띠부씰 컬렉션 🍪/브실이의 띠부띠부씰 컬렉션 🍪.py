from collections import Counter

N = int(input())
cnt = Counter(input())
ans = min(cnt['E'], cnt['R']) >> 1
for c in "BONZSILV":
    ans = min(ans, cnt[c])
print(ans)