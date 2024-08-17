import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = []
N, K = g()
if N:
    A = g()
    for i in range(1, N):
        B = g()
        for s in range(K - 1):
            for t in range(s + 1, K):
                if (A[s] - A[t]) % 12 == 7 and (B[s] - B[t]) % 12 == 7 and A[s] != B[s] and A[t] != B[t]:
                    ans.append((i, s + 1, t + 1))
        A = B
if ans:
    for l in ans:
        print(*l)
else:
    print("POLE")