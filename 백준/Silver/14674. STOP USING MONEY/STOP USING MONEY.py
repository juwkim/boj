g = lambda: tuple(map(int, input().split()))

N, K = g()
games = [g() for _ in range(N)]
games.sort(key=lambda x: ((-(x[2] // x[1]), -(x[2] % x[1])), x[1], x[0]))
for game in games[:K]:
    print(game[0])