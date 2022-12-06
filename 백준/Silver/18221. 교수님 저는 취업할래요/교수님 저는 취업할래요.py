N = int(input())
board = []
pos = [(), ()]
for i in range(N):
    row = input()
    board.append([*map(int, row.split())])
    for j in range(2):
        if not pos[j]:
            idx = row.find(str(3 * j + 2))
            if idx != -1:
                pos[j] = (i, idx // 2)
if (pos[0][0] - pos[1][0]) ** 2 + (pos[0][1] - pos[1][1]) ** 2 < 25:
    print(0)
else:
    x1, x2 = sorted([pos[0][0], pos[1][0]])
    y1, y2 = sorted([pos[0][1], pos[1][1]])
    a = sum(sum(board[i][y1:y2+1]) for i in range(x1, x2 + 1))
    print(+(a >= 10))