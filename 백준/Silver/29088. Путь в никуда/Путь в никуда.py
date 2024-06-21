n, m, x, y = map(int, open(0).read().split())
d = min(x - 1, y - 1, n - x, m - y)
ans = 2 * d * (2 * d + 1) + 1
x, y = x - d, y + d
dist = 2 * d + 1
for dx, dy in zip((1, 0, -1, 0), (0, -1, 0, 1)):
    nx, ny = x + dx * dist, y + dy * dist
    if nx <= 0: ans += x - 1; break
    if nx > n:  ans += n - x; break
    if ny <= 0: ans += y - 1; break
    if ny > m:  ans += m - y; break
    x, y = nx, ny
    ans += dist
    if (dx, dy) == (0, -1):
        dist += 1
print(ans)