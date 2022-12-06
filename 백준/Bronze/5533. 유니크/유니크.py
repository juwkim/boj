N = int(input())
scores = [0 for _ in range(N)]
games = [*zip(*[[*map(int, input().split())] for _ in range(N)])]
for game in games:
    for j in range(N):
        if game.count(game[j]) == 1:
            scores[j] += game[j]
print(*scores)