g = lambda: [*map(int, input().split())]

r, c = g()
margin = [[-1] * (c + 2)]
a = margin + [[-1] + g() + [-1] for _ in range(r)] + margin

for i in range(1, r + 1):
    for j in range(1, c + 1):
        print(+all(a[i][j] < a[s][t] for s, t in ((i-1, j), (i+1, j), (i, j-1), (i, j+1))), end=' ')
    print()    