import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

jump = [*zip((-1, -1, -1, 0, 1, 1, 1, 0), (-1, 0, 1, 1, 1, 0, -1, -1))]
for _ in range(int(input())):
    n, d = g()
    t, d = n >> 1, d // 45 % 8
    a = [g() for _ in range(n)]
    for i in range(1, t + 1):
        idx = [(t + i * p, t + i * q) for p, q in jump]
        nums = [a[nx][ny] for nx, ny in idx]
        for j, (nx, ny) in enumerate(idx):
            a[nx][ny] = nums[j - d]
    for r in a:
        print(*r)