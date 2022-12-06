k, x, y = map(int, [input() for _ in range(3)])
cnt = y // x
lo = cnt * x
hi = cnt * (x + k - 1)
if y <= hi:
    ans = y
else:
    ans = x * (cnt + 1)

print(ans)