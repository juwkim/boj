import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = len(set(sum(g()) for _ in range(int(input()))))
print(ans)