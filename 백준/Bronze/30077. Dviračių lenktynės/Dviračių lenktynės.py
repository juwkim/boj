N, M, L, *T = map(int, open(0).read().split())
limit_time = M * min(T)
print(sum(t * (M - 1) < limit_time for t in T))