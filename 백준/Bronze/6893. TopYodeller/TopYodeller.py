g = lambda: [*map(int, input().split())]

n, k = g()
scores = [[0] * n]
for _ in range(k):
    scores.append([score + before for score, before in zip(g(), scores[-1])])
top_score = max(scores[-1])
for i in range(n):
    if scores[-1][i] == top_score:
        worst_rank = max(sum(score > line[i] for score in line) for line in scores) + 1
        print(f"Yodeller {i + 1} is the TopYodeller: score {scores[-1][i]}, worst rank {worst_rank}")