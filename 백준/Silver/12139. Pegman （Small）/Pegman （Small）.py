import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    l, r, u, d = [], [], [], []
    for line in board:
        left = C
        for i in range(C):
            if line[i] in "><^v":
                left = i
                break
        l.append(left)
        right = -1
        for i in range(C - 1, -1, -1):
            if line[i] in "><^v":
                right = i
                break
        r.append(right)
    for line in zip(*board):
        up = R
        for i in range(R):
            if line[i] in "><^v":
                up = i
                break
        u.append(up)
        down = -1
        for i in range(R - 1, -1, -1):
            if line[i] in "><^v":
                down = i
                break
        d.append(down)
    ans = 0
    for i in range(R):
        for j in range(C):
            match board[i][j]:
                case ".":
                    continue
                case "<":
                    if (l[i], r[i], u[j], d[j]) == (j, j, i, i):
                        ans = "IMPOSSIBLE"
                        break
                    if j > l[i]:
                        continue
                    ans += 1
                case ">":
                    if (l[i], r[i], u[j], d[j]) == (j, j, i, i):
                        ans = "IMPOSSIBLE"
                        break
                    if j < r[i]:
                        continue
                    ans += 1
                case "^":
                    if (l[i], r[i], u[j], d[j]) == (j, j, i, i):
                        ans = "IMPOSSIBLE"
                        break
                    if i > u[j]:
                        continue
                    ans += 1
                case "v":
                    if (l[i], r[i], u[j], d[j]) == (j, j, i, i):
                        ans = "IMPOSSIBLE"
                        break
                    if i < d[j]:
                        continue
                    ans += 1                        
    print(f"Case #{tc}: {ans}")