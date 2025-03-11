n, g = map(int, input().split())
s = [[*map(int, input())] for _ in range(n)]
input()
e = [[*map(int, input())] for _ in range(n)]
ans = -1
for bits in range(64):
    cur = [s[i][:] for i in range(n)]
    for _ in range(g):
        new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cnt = cur[i][j]
                if i > 0: cnt += cur[i - 1][j]
                if i < n - 1: cnt += cur[i + 1][j]
                if j > 0: cnt += cur[i][j - 1]
                if j < n - 1: cnt += cur[i][j + 1]
                new[i][j] = (bits >> cnt) & 1
        cur = new
    if cur == e:
        ans = bits
        break
print(ans)