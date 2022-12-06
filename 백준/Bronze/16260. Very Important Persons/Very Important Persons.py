g = lambda: [*map(int, input().split())]


for _ in range(int(input())):
    n, m = g()
    i, j = 0, 0
    buf = [[0] * m for _ in range(n)]
    i_check = set(range(n))
    j_check = set(range(m))
    for num in range(n * m, 0, -1):
        buf[i][j] = num
        if i - 1 in i_check and j + 1 in j_check and buf[i-1][j+1] == 0:
            i -= 1
            j += 1
        elif i + 1 in i_check and j - 1 in j_check and buf[i+1][j-1] == 0:
            i += 1
            j -= 1
        elif i + 1 in i_check and j + 1 in j_check:
            if i > j:
                i += 1
            else:
                j += 1
        elif i + 1 in i_check:
            i += 1
        else:
            j += 1
    for line in buf:
        print(*line)