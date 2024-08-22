def solve(l, r):
    if r < l:
        return 0
    return r * (r + 1) // 2 - l * (l - 1) // 2

n, k = map(int, input().split())
a = [*map(int, input().split())]
if n == 1:
    ans = solve(max(0, a[0] - k + 1), a[0])
else:
    max1, max2 = -1, -1
    for num in a:
        if num > max1:
            max1, max2 = num, max1
        elif num > max2:
            max2 = num
    l = max1 - max2 + 1
    ans = solve(max2, max1) * (k // l) + solve(max1 - k % l + 1, max1)
print(ans)