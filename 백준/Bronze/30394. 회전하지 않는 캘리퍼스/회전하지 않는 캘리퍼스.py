import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

y = [g()[1] for _ in range(int(input()))]
print(max(y) - min(y))