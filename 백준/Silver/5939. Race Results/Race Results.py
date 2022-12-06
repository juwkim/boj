import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

res = [g() for _ in range(int(input()))]
res.sort()
for line in res:
    print(*line)