def solve(l, r):
    if r - l == 0:
        return 0
    if r - l == 1:
        return l * r
    d = (r - l) // 2
    return solve(l, l + d) + solve(l + d + 1, r)
print(solve(1, int(input())))