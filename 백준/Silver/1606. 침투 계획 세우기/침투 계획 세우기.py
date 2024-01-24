x, y = map(int, input().split())
ans = 3 * (x + y) * (x + y + 1) + 1
if y:
    ans += y - 6 * (x + y)
print(ans)