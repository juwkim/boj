import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K, N = map(int, input().split())
    def solve(N):
        if N == 1:
            return 1, 1
        p, q = solve(N // 2)
        if N & 1:
            return p + q, q
        return p, p + q
    p, q = solve(N)
    print(f"{K} {p}/{q}")