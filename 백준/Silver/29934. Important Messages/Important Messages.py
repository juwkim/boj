import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

a = set(input() for _ in range(int(input())))
ans = 0
for _ in range(int(input())):
    ans += input() in a
print(ans)