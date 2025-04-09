import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

for _ in range(int(input())):
    a, b = input() + '.', input()
    cnt1 = Counter(a[:len(b)])
    cnt2 = Counter(b)
    ans = "NO"
    for i in range(len(b), len(a)):
        if all(cnt1[k] == cnt2[k] for k in cnt2):
            ans = "YES"
            break
        cnt1[a[i]] += 1
        cnt1[a[i - len(b)]] -= 1
    print(ans)