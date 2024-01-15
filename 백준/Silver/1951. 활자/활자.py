import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
ans, cur = 0, 10
while N >= cur:
    ans += (cur - cur // 10) * (len(str(cur)) - 1)
    ans %= 1234567
    cur *= 10
ans += (N - cur // 10 + 1) * (len(str(cur)) - 1)
ans %= 1234567
print(ans)