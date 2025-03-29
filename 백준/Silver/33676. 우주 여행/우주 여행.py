g = lambda: map(int, input().split())

N, M, K, L = g()
if L < N + M - 2 or (N ^ M ^ L) & 1:
    print(-1)
else:
    print((N - 1) * 'D' + (L - N - M + 2) // 2 * 'RL' + (M - 1) * 'R')