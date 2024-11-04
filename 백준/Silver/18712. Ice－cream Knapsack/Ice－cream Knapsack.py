import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, K = map(int, input().split())
    C, H = g(), g()
    idx = sorted(range(N), key=lambda i: C[i])
    end = K - 1
    MAX_CAL = C[idx[end]]
    while end + 1 < N and C[idx[end + 1]] == C[idx[end]]:
        end += 1
    print(MAX_CAL, sum(sorted(H[i] for i in idx[:end + 1])[-K:]))