import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
cnt = int(input())
ans = 0
if N == 1:
    ans = cnt * 8
elif N == 5:
    ans = cnt * 8 + 4
elif N == 2:
    q, r = divmod(cnt, 2)
    if r:
        ans = q * 8 + 7
    else:
        ans = q * 8 + 1
elif N == 3:
    q, r = divmod(cnt, 2)
    if r:
        ans = q * 8 + 6
    else:
        ans = q * 8 + 2
elif N == 4:
    q, r = divmod(cnt, 2)
    if r:
        ans = q * 8 + 5
    else:
        ans = q * 8 + 3
print(ans)