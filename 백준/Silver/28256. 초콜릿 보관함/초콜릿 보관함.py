import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    board = [input() for _ in range(3)]
    n, *a = map(int, input().split())
    nums, cnt = [], 0
    for i, j in ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)):
        if board[i][j] == 'O':
            cnt += 1
        else:
            if cnt:
                nums.append(cnt)
            cnt = 0
    if cnt:
        if nums and board[0][0] == 'O':
            nums[0] += cnt
        else:
            nums.append(cnt)
    print(+(a == sorted(nums)))