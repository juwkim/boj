import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

w, _, h, _ = [int(input()) for _ in range(4)]
print(w * h)