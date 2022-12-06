N = int(input())
cnt = 0
cows = [[*map(int, input())] for _ in range(N)]
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if cows[i][j]:
            cnt += 1
            for x in range(i+1):
                for y in range(j+1):
                    cows[x][y] ^= 1
print(cnt)