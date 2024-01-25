import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    M, N, P = g()
    check = [[[-1, 0] for _ in range(M + 1)] for _ in range(P + 1)]
    for _ in range(N):
        p, m, t, j = input().split()
        p, t, j = map(int, [p, t, j])
        m = ord(m) - ord('A')
        if check[p][m][0] != -1:
            continue
        if j:
            check[p][m][0] = t
        else:
            check[p][m][1] += 1
    res = [[0, 0] for _ in range(P + 1)]
    for i in range(1, P + 1):
        solved, score = 0, 0
        for time, cnt in check[i]:
            if time != -1:
                solved += 1
                score += time + 20 * cnt
        res[i] = [solved, score]
    print(f"Data Set {tc}:")
    for id in sorted(range(1, P + 1), key=lambda x: (-res[x][0], res[x][1])):
        print(id, res[id][0], res[id][1])
    print()