from itertools import product

W, R = map(int, input().split())
S = (W - 1) // 2
ans = [[0] * W for _ in range(R)]
for p, (i, j) in enumerate(sorted(product(range(R), range(W)), key=lambda x: ((R - 1 - x[0]) ** 2 + (S - x[1]) ** 2, -x[0], x[1])), 1):
    ans[i][j] = p
for l in ans:
    print(*l)