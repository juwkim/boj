import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
ans = 0
for _ in range(n):
    a, b = input().replace(' ', ''), input().replace(' ', '')
    cnt1 = sum(c in "aeiouy" for c in a)
    cnt2 = sum(c in "aeiouy" for c in b)
    if cnt1 == cnt2 and len(a) >= k and len(b) >= k and a[-k:] == b[-k:]:
        ans += 1
print(ans)