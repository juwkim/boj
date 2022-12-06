g = lambda: [*map(int, input().split())]

N, NQ, P = g()
ans = [g() for _ in range(N)]
idxs = set(range(N))
for _ in range(P):
    Q, A = g()
    temp = set()
    for idx in idxs:
        if ans[idx][Q-1] != A:
            temp.add(idx)
    idxs -= temp
print(len(idxs))