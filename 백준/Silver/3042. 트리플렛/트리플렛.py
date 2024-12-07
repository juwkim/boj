from itertools import combinations

N = int(input())
a = [input() for _ in range(N)]
l = [(i, j) for i in range(N) for j in range(N) if a[i][j] != '.']
print(sum((i1 - i2) * (j1 - j3) == (i1 - i3) * (j1 - j2) for (i1, j1), (i2, j2), (i3, j3) in combinations(l, 3)))