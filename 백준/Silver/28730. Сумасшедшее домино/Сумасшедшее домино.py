n = int(input())
ans = [['' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if ans[i][j] != '':
            continue
        if j + 1 != n and ans[i][j + 1] == '':
            ans[i][j], ans[i][j + 1] = '.', '.'
            if i + 1 != n:
                ans[i + 1][j] = "#"
        elif i + 1 != n and ans[i + 1][j] == '':
            ans[i][j], ans[i + 1][j] = '.', '.'
            if j + 1 != n and ans[i][j + 1] != '.':
                ans[i][j + 1] = "#"
for row in ans:
    for c in row:
        if c == '':
            print('#', end='')
        else:
            print(c, end='')
    print()