import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
A = ["X" * (C + 2)] + ["X" + input() + "X" for _ in range(R)] + ["X" * (C + 2)]
ans = 0
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if A[i][j] == "." and sum(A[x][y] == "X" for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))) == 3:
            ans = 1
            break
    if ans:
        break
print(ans)