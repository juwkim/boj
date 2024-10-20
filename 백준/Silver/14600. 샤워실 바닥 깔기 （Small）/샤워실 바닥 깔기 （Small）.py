K, x, y = map(int, open(0).read().split())
i, j = 2 ** K - y, x - 1
if K == 1:
    ans = [[1, 1], [1, 1]]
    ans[i][j] = -1
else:
    ans = [[1, 1, 2, 2], [1, 3, 3, 2], [4, 3, 3, 5], [4, 4, 5, 5]]
    ans[i][j] = -1
    if i in (1, 2) and j in (1, 2):
        pass
    elif i <= 1 and j <= 1:
        ans[1][1] = 1
    elif i <= 1 and j >= 2:
        ans[1][2] = 2
    elif i >= 2 and j <= 1:
        ans[2][1] = 4
    else:
        ans[2][2] = 5
for l in ans:
    print(*l)