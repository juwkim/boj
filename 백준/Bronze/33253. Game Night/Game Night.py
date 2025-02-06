from collections import Counter

input()
cnt1 = Counter(input())
cnt2 = Counter(input())
ans = sum(max(0, cnt2[k] - cnt1[k]) for k in cnt2)
print(ans)