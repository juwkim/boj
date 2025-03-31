from string import ascii_uppercase

l = [*map(str.rstrip, open(0))]
for i in range(0, len(l), 2):
    n = (int(l[i][:2]) - 1) % 100 + 1
    text = list(l[i+1].upper() + (n**2 - len(l[i+1]) + 25) // 26 * ascii_uppercase)
    mat = [text[i:i+n] for i in range(0, n**2, n)]
    for k in l[i][2:]:
        match k:
            case 'S':
                for j in range(n):
                    if j & 1:
                        c = mat[n - 1][j]
                        for i in range(n - 1, 0, -1):
                            mat[i][j] = mat[i - 1][j]
                        mat[0][j] = c
                    else:
                        c = mat[0][j]
                        for i in range(n - 1):
                            mat[i][j] = mat[i + 1][j]
                        mat[n - 1][j] = c
            case 'R':
                for i in range(n):
                    if i & 1:
                        mat[i] = mat[i][1:] + [mat[i][0]]
                    else:
                        mat[i] = [mat[i][-1]] + mat[i][:-1]
            case 'L':
                new = [[''] * n for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        d = min(i, j, n - 1 - i, n - 1 - j)
                        if d & 1:
                            if d == i and j > d:
                                ni, nj = i, j - 1
                            elif d == j and i < n - 1 - d:
                                ni, nj = i + 1, j
                            elif d == n - 1 - i and j < n - 1 - d:
                                ni, nj = i, j + 1
                            else:
                                ni, nj = i - 1, j
                        else:
                            if d == i and j < n - 1 - d:
                                ni, nj = i, j + 1
                            elif d == j and i > d:
                                ni, nj = i - 1, j
                            elif d == n - 1 - i and j > d:
                                ni, nj = i, j - 1
                            else:
                                ni, nj = i + 1, j
                        new[ni][nj] = mat[i][j]
                mat = new
    print("".join(sum(mat, [])))