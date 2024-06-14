a = [[*map(int, l.split())] for l in open(0)]

ans = 0
def solve(i):
    if i == 9:
        return 1
    x, y = divmod(i, 3)
    if a[x][y]:
        return solve(i + 1)
    s = set(range(1, 10))
    for j in range(3):
        s.discard(a[x][j])
        s.discard(a[j][y])
    ret = 0
    for num in s:
        a[x][y] = num
        ret += solve(i + 1)
        a[x][y] = 0
    return ret
print(solve(0))