g = lambda: [*map(int, input().split())]

N, M = g()
S = g() + [0] * M
for i in range(N):
    for j, num in enumerate(g()):
        S[i] -= num
        S[j] += num
print(*S)