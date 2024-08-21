import sys
g = lambda: map(int, sys.stdin.readline().split())

n, b = map(int, input().split())
ans, Sum = 0, 0
for i, num in enumerate(g()):
    ans -= i * num
    Sum += num
    val = min(Sum, b)
    ans += (i + 1) * val
    Sum -= val
ans += (n + 1) * Sum
print(ans)