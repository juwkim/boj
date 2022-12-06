g = lambda: [*map(int, input().split())]

from bisect import bisect_left
n, m = g()
poses = g()
trees = sorted(g())
check = [0 for _ in range(m)]
for pos in poses:
    idx = bisect_left(trees, pos)
    if idx == 0:
        check[0] = 1
    elif idx == m:
        check[m-1] = 1
    elif abs(trees[idx] - pos) < abs(trees[idx-1] - pos):
        check[idx] = 1
    else:
        check[idx-1] = 1

print(n - sum(check))