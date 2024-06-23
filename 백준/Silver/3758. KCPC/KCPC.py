import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    n, k, t, m = g()
    score = [[0] * (k + 1) for _ in range(n + 1)]
    log = [[0, 0] for _ in range(n + 1)]
    for time in range(m):
        i, j, s = g()
        score[i][j] = max(score[i][j], s)
        log[i][0] += 1
        log[i][1] = time
    l = sorted(range(1, n + 1), key=lambda x: (-sum(score[x]), log[x]))
    print(l.index(t) + 1)