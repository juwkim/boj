import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

buf = [g() for _ in range(int(input()))]
buf.sort(key=lambda x: (-x[0], x[1]))
print(*buf[0], *buf[1])
buf.sort(key=lambda x: (x[1], -x[0]))
print(*buf[0], *buf[1])