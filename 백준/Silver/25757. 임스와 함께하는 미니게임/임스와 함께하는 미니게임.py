N, game = input().split()
idx = "YFO".index(game) + 1
print(len({input() for _ in range(int(N))}) // idx) 