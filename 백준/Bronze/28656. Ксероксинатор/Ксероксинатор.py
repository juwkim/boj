import sys
g = lambda: map(int, sys.stdin.readline().split())

n, b = map(int, input().split())
ans, Sum = 0, 0
for i, num in enumerate(g()):
    val = min(Sum + num, b)
    ans += i * (val - num) + val
    Sum -= val - num
ans += (n + 1) * Sum
print(ans)