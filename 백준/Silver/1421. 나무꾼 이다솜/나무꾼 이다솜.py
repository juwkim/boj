N, C, W, *L = map(int, open(0).read().split())
print(max(sum(max(0, (tree - tree % i) * W - (tree // i - (tree % i == 0)) * C) for tree in L) for i in range(1, max(L) + 1)))