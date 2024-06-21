pos = (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5)
idx = {pos[i]: i + 1 for i in range(33)}
target_idxs = pos[::-1]
N, *nums = map(int, open(0).read().split())
p = 0
while p < len(nums):
    board = [[0] * 9 for _ in range(9)]
    while nums[p] != 0:
        x, y = pos[nums[p] - 1]
        board[x][y] = 1
        p += 1
    p += 1
    while True:
        jump = False
        for i, j in target_idxs:
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