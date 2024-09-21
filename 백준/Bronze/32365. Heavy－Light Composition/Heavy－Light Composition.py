import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

T, N = map(int, input().split())
for _ in range(T):
    cnt = Counter(s:=input())
    cur = cnt[s[0]] < 2
    ans = 'T'
    for c in s[1:]:
        if (cnt[c] < 2) == cur:
            ans = 'F'
            break
        cur = cnt[c] < 2
    print(ans)