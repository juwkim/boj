from collections import Counter

n = int(input())
cnt = Counter(input())
ans = min(cnt[i] for i in "uospc")
print(ans)