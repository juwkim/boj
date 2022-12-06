g = lambda: [*map(int, input().split())]

import copy
N = int(input())
Map = [[0] * (N + 1) for _ in range(N + 1)]
score = [0] * (N + 1)
for i in range(1, N + 1):
    for j, num in enumerate(g(), 1):
        Map[i][num] = N - j
        score[num] += N - j
print(*sorted(range(1, N + 1), key=lambda x: (-score[x], x))[:3])

new_Map = copy.deepcopy(Map)
for i in range(1, N):
    for j in range(i + 1, N + 1):
        if Map[i][j] and Map[i][j] == Map[j][i]:
            new_Map[i] = [0] * (N + 1)
            new_Map[j] = [0] * (N + 1)

score = [sum(line) for line in zip(*new_Map)]
print(*sorted(range(1, N + 1), key=lambda x: (-score[x], x))[:3])