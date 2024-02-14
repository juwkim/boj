import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N, M, A = map(int, input().split())
    if A > N * M:
        ans = "IMPOSSIBLE"
    elif A == N * M:
        ans = f"0 0 {N} 0 0 {M}"
    else:
        ans = f"0 0 {N} 1 {N - A % N} {A // N + 1}"
    print(f"Case #{tc}: {ans}")