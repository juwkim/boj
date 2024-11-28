import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

r, c = g()
A = [g() for _ in range(r)]
s, t = g()
B = [input() for _ in range(s)]
def solve():
    Min = 1e9
    n, m = len(B), len(B[0])
    for i in range(r - n + 1):
        for j in range(c - m + 1):
            cnt = sum(A[i + x][j + y] for x in range(n) for y in range(m) if B[x][y] == '#')
            Min = min(Min, cnt)
    return Min
Min = solve()
for i in range(3):
    B = [l[::-1] for l in zip(*B)]
    Min = min(Min, solve())
ans = sum(sum(l) for l in A) - Min
print(ans)