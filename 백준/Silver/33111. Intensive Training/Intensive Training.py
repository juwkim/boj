import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, R, K = map(int, input().split())
    q1, r1 = divmod(R, N)
    q2, r2 = divmod(K, N)
    if r1 + r2 > N:
        ans = (N - r2) * (q1 + 1) * q2 + (N - r1) * (q2 + 1) * q1 + (r1 + r2 - N) * (q1 + 1) * (q2 + 1)
    else:
        ans = r1 * (q1 + 1) * q2 + r2 * (q2 + 1) * q1 + (N - r1 - r2) * q1 * q2
    print(ans)