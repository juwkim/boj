g = lambda: [*map(int, input().split())]
M, F = g()
buls = [input() for _ in range(M)]
cows = [input() for _ in range(F)]
alls = buls + cows

for i in range(M):
    for j in range(F):
        cnt = -2
        bul = buls[i]
        cow = cows[j]
        for k in range(F + M):
            cnt += all(a in b + c for a, b, c in zip(alls[k], bul, cow))
        print(cnt, end=' ')
    print()