r, n = map(int, input().split())
rows = [[*input()] for _ in range(r + 3)]
for c in map(chr, range(97, 97 + n)):
    x = min(range(r + 3), key=lambda i: (all(c != '-' for c in rows[i]), i not in (1, r // 2 + 2), -rows[i].count('-'), min(abs(i - e) for e in (0, r // 2 + 1, r + 2)), i))
    for group in (4, 6), (2, 8), (0, 10), (5,), (1, 9):
        can = [i for i in group if rows[x][i] == '-']
        if can:
            if len(can) > 1 and sum(rows[i][j] == '-' for i in range(r + 3) for j in (6, 8, 9, 10)) > sum(rows[i][j] == '-' for i in range(r + 3) for j in (0, 1, 2, 4)):
                y = can[1]
            else:
                y = can[0]
            rows[x][y] = c
            break
for row in rows:
    print(*row, sep='')