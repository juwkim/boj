import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [[input() for _ in range(n)] for _ in range(10)]
num = [[0] * 10 for _ in range(10)]
for i in range(9):
    for j in range(i + 1, 10):
        cnt = sum(a[i][k][l] != a[j][k][l] for k in range(n) for l in range(m))
        num[i][j] = cnt
        num[j][i] = cnt
ans = num[0][2] + num[0][3] + num[0][5] + num[0][9]
for i in range(24 * 60 - 1):
    h1, m1 = divmod(i, 60)
    h2, m2 = divmod(i + 1, 60)
    (h11, h12), (m11, m12) = divmod(h1, 10), divmod(m1, 10)
    (h21, h22), (m21, m22) = divmod(h2, 10), divmod(m2, 10)
    ans += num[h11][h21] + num[h12][h22] + num[m11][m21] + num[m12][m22]
print(ans)