import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [[input() for _ in range(n)] for _ in range(10)]
dic = {(0, 2): 1, (0, 3): 1, (0, 5): 24, (0, 9): 146, (0, 0): 992, (0, 1): 172, (1, 2): 172, (2, 3): 171, (3, 4): 170, (4, 5): 170, (5, 6): 146, (6, 7): 146, (7, 8): 146, (8, 9): 146, (1, 1): 992, (2, 2): 632, (3, 3): 393, (4, 4): 334, (5, 5): 334, (6, 6): 118, (7, 7): 118, (8, 8): 118, (9, 9): 118}
ans = 0
for (i, j), v in dic.items():
    cnt = sum(a[i][k][l] != a[j][k][l] for k in range(n) for l in range(m))
    ans += cnt * v
print(ans)