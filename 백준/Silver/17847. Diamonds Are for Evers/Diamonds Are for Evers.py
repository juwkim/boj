from math import isqrt

s = input()
l = isqrt(len(s))
board = [list(s[i:i+l]) for i in range(0, len(s), l)]

ans = []
half = l // 2
for cnt in range(half, 0, -1):

    i, j = half, half - cnt    
    for di, dj in ((-1, 1), (1, 1), (1, -1), (-1, -1)):
        for _ in range(cnt):
            ans.append(board[i][j])
            i = i + di
            j = j + dj

ans.append(board[half][half])
print(*ans, sep='')