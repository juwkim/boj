N, M = map(int, [input(), input()])
target = [*map(int, input().split())]
score = [0]*N
for i in range(M):
    game = [*map(int, input().split())]
    for j in range(N):
        if target[i] == game[j]:
            score[j] += 1
        else:
            score[target[i]-1] += 1
print(*score, sep='\n')