import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [[input() for _ in range(n)] for _ in range(10)]
ans = 0
for i, j, v in ((0, 1, 172), (0, 2, 1), (0, 3, 1), (0, 5, 24), (0, 9, 146), (1, 2, 172), (2, 3, 171), (3, 4, 170), (4, 5, 170), (5, 6, 146), (6, 7, 146), (7, 8, 146), (8, 9, 146)):
    ans += v * sum(a[i][k][l] != a[j][k][l] for k in range(n) for l in range(m))
print(ans)