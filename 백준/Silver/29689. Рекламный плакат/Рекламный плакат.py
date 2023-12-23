import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
a = input()
ans = 1
for _ in range(n - 1):
    b = input()
    ans = max(ans, min(len(a), len(b)))
    a = b
print(ans)