import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, K, C, X = g()
    A, B = g(), g()
    M = [[(A[i] * (i + 1) + B[j] * (j + 1) + C) % X for j in range(N)] for i in range(N)]

    ans = sum(max(M[p][q] for p in range(i, i + K) for q in range(j, j + K)) for i in range(N - K + 1) for j in range(N - K + 1))
    print(f"Case #{tc}: {ans}")