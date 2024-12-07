import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
H = [input() for _ in range(n)]
R = [input() for _ in range(n)]
C = [input() for _ in range(n)]
M = [[[1] * n for _ in range(n)] for _ in range(n)]
for j in range(n):
    for k in range(n):
        if H[j][k] == '0':
            for i in range(n):
                M[i][j][k] = 0
for i in range(n):
    for k in range(n):
        if R[i][k] == '0':
            for j in range(n):
                M[i][j][k] = 0
for i in range(n):
    for j in range(n):
        if C[i][j] == '0':
            for k in range(n):
                M[i][j][k] = 0

def solve():
    for j in range(n):
        for k in range(n):
            if H[j][k] == '1' and all(M[i][j][k] == 0 for i in range(n)):
                return "NO"
    for i in range(n):
        for k in range(n):
            if R[i][k] == '1' and all(M[i][j][k] == 0 for j in range(n)):
                return "NO"
    for i in range(n):
        for j in range(n):
            if C[i][j] == '1' and all(M[i][j][k] == 0 for k in range(n)):
                return "NO"
    return "YES"

ans = solve()
print(ans)
if ans == "YES":
    for i in range(n):
        for j in range(n):
            print(*M[i][j], sep='')