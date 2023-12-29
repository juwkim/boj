import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, C = map(int, input().split())
Map = tuple(tuple(map(lambda c: 1 << ord(c) - ord('A'), input())) for _ in range(R))
ans, mask = 0, 0
mask |= Map[0][0]
def dfs(i, j):
    global ans, mask
    ans = max(ans, mask.bit_count())
    for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= a < R and 0 <= b < C and mask & Map[a][b] == 0:
            mask ^= Map[a][b]
            dfs(a, b)
            mask ^= Map[a][b]
dfs(0, 0)
print(ans)