r, s = map(lambda l: list(map(int, l)), input().split('%'))
M, N = len(r) >> 1, len(s)
R = [r[t] ^ r[t + M] for t in range(M)]
T = [s[i] ^ s[(i + M) % N] for i in range(N)]
for k in range(N):
    if all(T[(k + t) % N] == R[t] for t in range(M)):
        print(k)
        break