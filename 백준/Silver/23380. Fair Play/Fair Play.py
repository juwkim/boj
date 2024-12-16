import sys
input = sys.stdin.readline

n = int(input())
ans = "impossible"
if n % 2 == 0:
    (b0, p0), *l, (b1, p1) = sorted([*map(int, input().split())] for _ in range(n))
    s, t = b0 + b1, p0 + p1
    if all(l[i][0] + l[n - 3 - i][0] == s and l[i][1] + l[n - 3 - i][1] == t for i in range(n // 2 - 1)):
        ans = "possible"
print(ans)