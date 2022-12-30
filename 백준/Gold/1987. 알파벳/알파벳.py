def one(num):
    cnt = 0
    while num:
        num, r = divmod(num, 2)
        cnt += r
    return cnt

R, C = map(int, input().split())
Map = tuple(tuple(map(lambda c: 1 << ord(c) - 65, input())) for _ in range(R))
char_mask = 0
for line in Map:
    for c in line:
        char_mask |= c
ans_max = one(char_mask)
ans, mask = 0, 0
mask |= Map[0][0]
def dfs(i, j):
    global ans, mask
    ans = max(ans, one(mask))
    if ans == ans_max:
        return
    for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= a < R and 0 <= b < C and mask & Map[a][b] == 0:
            mask ^= Map[a][b]
            dfs(a, b)
            mask ^= Map[a][b]
dfs(0, 0)
print(ans)