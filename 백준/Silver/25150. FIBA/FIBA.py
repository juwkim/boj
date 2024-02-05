import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K, H = g()
team = [[0, 0] for _ in range(N + 1)] # point, score
res = []
for i in range(1, N):
    for j in range(i + 1, N + 1):
        a, b = g()
        if a > b:
            team[i][0] += 2
            team[j][0] += 1
            team[i][1] += a
            team[j][1] += b
        elif a < b:
            team[i][0] += 1
            team[j][0] += 2
            team[i][1] += a
            team[j][1] += b
        res.append((i, j))
rank = sorted(range(1, N + 1), key=lambda x: team[x], reverse=True)
print(team[H][0])
print(rank[0])
second_round = set(rank[:K])
point = 0
for i, j in res:
    if i in second_round and j in second_round:
        point += 3
print(point)