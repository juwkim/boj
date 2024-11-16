N, M = map(int, input().split())
S = [*map(int, input())]
for i in range(N - 1):
    if S[i] and M >= 10 - S[i]:
        M -= 10 - S[i]
        S[i] = 0
S[-1] = (S[-1] + M) % 10
print(*S, sep="")