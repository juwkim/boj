import sys
input = sys.stdin.readline

ans, s = 0, set()
dx = 2018, -2018, 0, 0, 1680, 1680, -1680, -1680, 1118, 1118, -1118, -1118
dy = 0, 0, 2018, -2018, 1118, -1118, 1118, -1118, 1680, -1680, 1680, -1680
t = [*zip(dx, dy)]
for i in range(int(input())):
    x, y = map(int, input().split())
    ans += sum((x + p, y + q) in s for p, q in t)
    s.add((x, y))
print(ans)