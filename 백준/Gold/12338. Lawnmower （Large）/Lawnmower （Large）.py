import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, int(input()) + 1):
    N, M = g()
    A = [g() for _ in range(N)]
    row_max = [max(row) for row in A]
    col_max = [max(col) for col in zip(*A)]
    if all(min(row_max[i], col_max[j]) == A[i][j] for i in range(N) for j in range(M)):
        ans = "YES"
    else:
        ans = "NO"
    print(f"Case #{tc}: {ans}")