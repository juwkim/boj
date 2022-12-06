g = lambda: [*map(int, input().split())]

N, T, P = g()
score = [N] * T
solve = [g() for _ in range(N)]
for i in range(N):
    for j in range(T):
        score[j] -= solve[i][j]

rank = [*range(N)]
rank.sort(key=lambda x: (-sum(i*j for i, j in zip(score, solve[x])), -sum(solve[x]), x))
print(sum(i*j for i, j in zip(score, solve[P-1])), rank.index(P-1) + 1)