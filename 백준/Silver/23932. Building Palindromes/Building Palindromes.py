import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, int(input()) + 1):
    N, Q = g()
    S = input()
    px = [[0] * 26 for _ in range(N + 1)]
    for i in range(N):
        px[i + 1] = px[i][:]
        px[i + 1][ord(S[i]) - 65] += 1
    ans = 0
    for _ in range(Q):
        L, R = g()
        ans += sum((px[R][c] ^ px[L - 1][c]) & 1 for c in range(26)) < 2
    print(f"Case #{tc}: {ans}")