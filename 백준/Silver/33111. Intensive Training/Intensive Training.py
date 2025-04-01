import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, R, K = map(int, input().split())
    q1, r1 = divmod(R, N)
    q2, r2 = divmod(K, N)
    print(N * q1 * q2 + r2 * q1 + r1 * q2 + max(0, r1 + r2 - N))