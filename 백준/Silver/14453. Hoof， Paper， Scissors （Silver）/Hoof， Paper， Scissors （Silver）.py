from collections import Counter

_, *A = map(str.rstrip, open(0))
cnt1, cnt2 = Counter(A), Counter()
ans = max(cnt1.values())
for a in A:
    cnt1[a] -= 1
    cnt2[a] += 1
    ans = max(ans, max(cnt1.values()) + max(cnt2.values()))
print(ans)