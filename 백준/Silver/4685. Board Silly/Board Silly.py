l = open(0).read().split()
for i in range(0, len(l), 9):
    *a, c = l[i:i+9]
    row, col = [8 - l.count('.') for l in a], [8 - l.count('.') for l in zip(*a)]
    tmp = ['.' * 7 + l + '.' * 7 for l in a]
    dig1 = [8 - l.count('.') for l in zip(*[tmp[i][7-i:22-i] for i in range(8)])] # i + j
    dig2 = [8 - l.count('.') for l in zip(*[tmp[i][i:i+15] for i in range(8)])] # j - i + 7
    printed = False
    for i in range(8):
        for j in range(8):
            if a[i][j] == c:
                for di, dj, cnt in (-1, 0, col[j]), (-1, 1, dig1[i + j]), (0, 1, row[i]), (1, 1, dig2[j - i + 7]), (1, 0, col[j]), (1, -1, dig1[i + j]), (0, -1, row[i]), (-1, -1, dig2[j - i + 7]):
                    ni, nj = i + cnt * di, j + cnt * dj
                    if 0 <= ni < 8 and 0 <= nj < 8 and a[ni][nj] != c and all(a[i + k * di][j + k * dj] in '.' + c for k in range(1, cnt)):
                        printed = True
                        print(f"{chr(ord('A') + i)}{j + 1}-{chr(ord('A') + ni)}{nj + 1}")
    if not printed:
        print("No moves are possible")
    print()