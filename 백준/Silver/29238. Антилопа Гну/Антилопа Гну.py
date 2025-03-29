x, y, f, g = map(int, open(0).read().split())
if (x, y) == (f, g):
    ans = 0
elif x == f:
    ans = (abs(y - g) - 1) * 3
elif y == g:
    ans = (abs(x - f) - 1) * 3
else:
    ans = (abs(x - f) - 1 + abs(y - g) - 1) * 3 + 1
print(ans)