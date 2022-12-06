g = lambda: [*map(int, input().split())]

n, m = g()
name = []
score = []

for _ in range(n):
    name.append(input())
    score.append(sum(g()))

min_score = min(score)
a = [i for i in range(n) if score[i] == min_score]
print(name[a[-1]])