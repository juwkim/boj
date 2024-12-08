import sys
input = sys.stdin.readline

N = int(input())
ans, T = 0, 0
for d, t in sorted([*map(int, input().split())] for _ in range(N)):
    T += t
    q, r = divmod(d, 7)
    day = q * 5 + min(r, 5)
    if T > 2 * day + 2 * q + (r == 6):
        ans = -1
        break
    ans = max(ans, T - day)
print(ans)