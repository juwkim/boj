def solve(x):
    global ans
    if x == 1:
        return
    if x % 3 == 0:
        y, z = x // 3, 2 * x // 3
    elif x % 2 == 0:
        y, z = x // 2, x // 2
    else:
        y, z = 1, x - 1
    ans += y * z
    solve(y)
    solve(z)

t, *nums = map(int, open(0).read().split())
for n in nums:
    ans = 0
    solve(n)
    print(ans)