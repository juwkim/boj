g = lambda: [*map(int, input().split())]

points = g()
score = [0, 0]
cur = 0
cur ^= (points[0] > points[1])
for i in range(points[cur]):
    score[cur] += 1
    print(*score, sep=':')

cur ^= 1
for i in range(points[cur]):
    score[cur] += 1
    print(*score, sep=':')