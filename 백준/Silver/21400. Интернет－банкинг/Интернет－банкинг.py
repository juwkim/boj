import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = [list(input()) for _ in range(n)]
p = list(input())
m = len(p)

ans = []
if any(all(p[j] != s[i][j] for i in range(n)) for j in range(m)):
    print(-1)
else:
    i = max(range(n), key=lambda i: sum(s[i][j] == p[j] for j in range(m)))
    for k in range(m):
        if s[i][k] != p[k]:
            j = 0
            while s[j][k] != p[k]:
                j += 1
            ans.append((i + 1, j + 1, k + 1))
    print(len(ans))
    for row in ans:
        print(*row)