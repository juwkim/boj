import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: {*map(int, input().split())}

ans = 0
prev = set()
for _ in range(int(input())):
    if not prev & (s := g()):
        ans += 1
    prev |= s
print(ans)