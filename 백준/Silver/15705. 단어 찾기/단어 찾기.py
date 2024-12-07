import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    S = input()
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] != S[0]:
                continue
            for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                for k in range(1, len(S)):
                    if 0 <= i + k * dx < N and 0 <= j + k * dy < M and A[i + k * dx][j + k * dy] == S[k]:
                        continue
                    break
                else:
                    return 1
    return 0
print(solve())