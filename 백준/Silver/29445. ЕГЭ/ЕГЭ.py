def solve(k, idx):
    if k == 0: return 0
    m = 1 << k - 1
    if idx < m: return solve(k - 1, idx)
    return solve(k - 1, idx - m) ^ 1

k, i = map(int, input().split())
print(*[solve(k, i + j - 1) for j in range(7)], sep='')