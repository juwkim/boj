g = lambda: [*map(int, input().split())]

*percent, n = g()
score = {'Lab': [0, 0], 'Hw': [0, 0], 'Proj': [0, 0], 'Exam': [0, 0]}
for _ in range(n):
    field, a, num = input().split()
    get, total = map(int, num.split('/'))
    score[field][0] += get
    score[field][1] += total

total = sum(i * j[0] / j[1] for i, j in zip(percent, score.values()))
print(int(total))