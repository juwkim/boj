y, m, d = map(int, input().split('-'))
t = y * 360 + (m - 1) * 30 + (d - 1) + int(input())
y, t = divmod(t, 360)
m, d = divmod(t, 30)
print(f"{y}-{m + 1:02d}-{d + 1:02d}")