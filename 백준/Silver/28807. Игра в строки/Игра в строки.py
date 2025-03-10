from collections import Counter

ans = "NO"
k = int(input())
s, t = input(), input()
cnt1 = Counter(t)
cnt2 = Counter(s[:k])
for i in range(len(s) - k + 1):
    if all(cnt2[c] <= cnt1[c] for c in cnt2):
        ans = "YES"
        break
    if i + k < len(s):
        cnt2[s[i + k]] += 1
        cnt2[s[i]] -= 1
print(ans)