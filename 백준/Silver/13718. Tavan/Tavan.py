g = lambda: [*map(int, input().split())]

N, M, K, X = g()
s = input()
board = [sorted(input()) for _ in range(M)]
ans = []
X -= 1
for line in board[::-1]:
    X, R = divmod(X, K)
    ans.append(line[R])

idx = -1
for c in s:
    if c == '#':
        print(ans[idx], end='')
        idx -= 1
    else:
        print(c, end='')