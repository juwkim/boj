import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

while n:= int(input()):
    points = [g() for _ in range(n)]
    a, b = points[n//2]
    score = [0, 0, 0]
    for s, t in points:
        val = (a - s) * (b - t)
        score[(val > 0) - (val < 0)] += 1
    print(*score[1:])