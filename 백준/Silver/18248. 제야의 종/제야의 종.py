import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
mat = [[1] * M for _ in range(M)]
def solve():
    for _ in range(N):
        zero, one = [], []
        for i, c in enumerate(g()):
            if c:
                one.append(i)
            else:
                zero.append(i)
        for p in one:
            for q in zero:
                if mat[p][q] == -1:
                    return "NO"
                mat[q][p] = -1
    return "YES"
print(solve())