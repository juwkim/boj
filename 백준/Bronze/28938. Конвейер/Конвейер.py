import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
s = sum(g())
if s > 0:
    print("Right")
elif s < 0:
    print("Left")
else:
    print("Stay")