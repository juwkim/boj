n, a, b, d = map(int, input().split())
def solve(x, y):
    if x == 0 or y == 0 or d == 1 or d > x + y:
        return 0
    l = x if d > x else d - 1
    r = d - y if d > y else 1
    return l - r + 1
ans = (a + d <= n) + (b + d <= n) + (a - d >= 1) + (b - d >= 1)
ans += sum(solve(p, q) for p, q in ((n - a, n - b), (n - b, a - 1), (n - a, b - 1), (a - 1, b - 1)))
print(ans)