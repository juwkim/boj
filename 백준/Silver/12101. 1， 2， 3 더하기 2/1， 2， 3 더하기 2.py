n, k = map(int, input().split())
def solve(c, l):
    global k
    if c == n:
        k -= 1
        if k == 0:
            print(*l, sep='+')
            exit()
    for i in range(1, 4):
        if c + i <= n:
            solve(c + i, l + [i])
solve(0, [])
print(-1)