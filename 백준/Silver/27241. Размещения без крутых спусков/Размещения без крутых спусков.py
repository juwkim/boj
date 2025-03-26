n, k = map(int, open(0))
ans = []
def solve(l):
    if len(l) == k:
        print(*l)
        return
    for i in range(max(1, l[-1] - 1), n + 1):
        if i not in l:
            solve(l + [i])
for i in range(1, n + 1):
    solve([i])