g = lambda: [*map(int, input().split())]

N, M = g()
player = [*zip(*[sorted(g()) for _ in range(N)])]
score = [0 for _ in range(N)]
for play in player:
    Max = max(play)
    idxs = [i for i in range(N) if play[i] == Max]
    for idx in idxs:
        score[idx] += 1
Max = max(score)
for i in range(N):
    if score[i] == Max:
        print(i+1, end=' ')