import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

A, B, K = g()
l = [[1] * B for _ in range(A)]
for _ in range(K):
    R, S, P, T = g()
    R -= 1
    S -= 1
    t = P >> 1
    if T:
        for i in range(A):
            for j in range(B):
                if R - t <= i <= R + t and S - t <= j <= S + t:
                    continue
                l[i][j] = 0
    else:
        for i in range(A):
            for j in range(B):
                if R - t <= i <= R + t and S - t <= j <= S + t:
                    l[i][j] = 0
print(sum(sum(x) for x in l))