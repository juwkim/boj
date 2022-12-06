d, m, y, n = map(int, input().split())
s = d + m * 30 + y * 360
d, m, y = map(int, input().split())
t = d + m * 30 + y * 360

diff = t - s
ans = (n + diff - 1) % 7 + 1
print(ans)