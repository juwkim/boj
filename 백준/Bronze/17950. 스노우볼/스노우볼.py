import sys
H, x = map(int, sys.stdin.readline().split())
balls = sys.stdin.readlines()
top, t = int(balls[-1]), 10**9 + 7
for i in range(H - 2, -1, -1):
    top = top * x % t + int(balls[i])
print(top * x % t)