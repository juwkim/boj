pos = ((7, 5), (7, 4), (7, 3), (6, 5), (6, 4), (6, 3), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (2, 5), (2, 4), (2, 3), (1, 5), (1, 4), (1, 3))
idx = {pos[i]: 33 - i for i in range(33)}
N, *nums = map(int, open(0).read().split())
p = 0
while p < len(nums):
    board = [[0] * 9 for _ in range(9)]
    while nums[p] != 0:
        x, y = pos[33 - nums[p]]
        board[x][y] = 1
        p += 1
    p += 1
    while True:
        jump = False
        for i, j in pos:
            if board[i][j]:
                continue
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if board[i + di][j + dj] and board[i + 2 * di][j + 2 * dj]:
                    board[i][j] = 1
                    board[i + di][j + dj] = 0
                    board[i + 2 * di][j + 2 * dj] = 0
                    jump = True
                    break
            if jump:
                break
        if not jump:
            break
    ans = sum(idx[(i, j)] for i in range(1, 8) for j in range(1, 8) if board[i][j])
    print(ans)