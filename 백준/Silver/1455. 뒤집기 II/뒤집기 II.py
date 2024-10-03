import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = [[*map(int, input())] for _ in range(N)]
ans = 0
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if A[i][j] == 1:
            ans += 1
            for x in range(i + 1):
                for y in range(j + 1):
                    A[x][y] ^= 1
print(ans)