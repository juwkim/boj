import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    n, B = int(input()), int(input())
    x, y = g()
    r = [0] * n
    for i in range(n):
        x1, y1, s = g()
        r[i] = s / ((x - x1) ** 2 + (y - y1) ** 2)
    p = 6 * (B + sum(r))
    ans = [i + 1 for i in range(n) if 7 * r[i] > p]
    if ans:
        print(*ans)
    else:
        print("NOISE")