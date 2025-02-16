L, R = map(int, input().split())
d = [0] * (R + 1)
for i in range(1, R + 1):
    for j in range(i, R + 1, i):
        d[j] += 1
M = max(d[L:R + 1])
S = [i for i in range(L, R + 1) if d[i] == M]
print(M, len(S))
print(*S, sep='\n')