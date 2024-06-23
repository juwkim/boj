import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

for _ in range(int(input())):
    cnt = Counter(s:=[*input()])
    n = len(s)
    if sum(v & 1 for v in cnt.values()) > (n & 1):
        print("Impossible")
        continue
    ans = 0
    l, r = 0, n - 1
    while l < r:
        if s[l] == s[r]:
            l, r = l + 1, r - 1
            continue
        k = r - 1
        while k > l and s[k] != s[l]:
            k -= 1
        if k == l:
            s[l], s[l + 1] = s[l + 1], s[l]
            ans += 1
        else:
            s.insert(r, s.pop(k))
            ans += r - k
            l, r = l + 1, r - 1
    print(ans)