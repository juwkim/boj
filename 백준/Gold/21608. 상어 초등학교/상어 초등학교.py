import sys
input = sys.stdin.readline

N = int(input())
room = [[-1] * (N + 2)] + [[-1] + [0] * N + [-1] for _ in range(N)] + [[-1] * (N + 2)]
students = [[] for _ in range(N * N + 1)]
for _ in range(N * N):
    num, *nums = map(int, input().split())
    likes = {*nums}
    students[num] = likes
    x, y = 1, 1
    key = (-1, -1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if room[i][j]:
                continue
            cur_like, cur_empty = 0, 0
            for nx, ny in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if room[nx][ny] in likes:
                    cur_like += 1
                elif room[nx][ny] == 0:
                    cur_empty += 1
            if (cur_like, cur_empty) > key:
                key = (cur_like, cur_empty)
                x, y = i, j
    room[x][y] = num
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        like = sum(room[nx][ny] in students[room[i][j]] for nx, ny in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
        ans += (0, 1, 10, 100, 1000)[like]
print(ans)