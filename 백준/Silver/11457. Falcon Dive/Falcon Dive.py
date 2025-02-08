import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    p = []
    for i in range(M):
        for j, c in enumerate(input()):
            if c == C:
                p.append((i, j))
            else:
                l[i][j] = c
    input()
    return p

while True:
    M, N, *C = input().split()
    M, N = map(int, (M, N))
    if M == 0:
        break
    C = C[0][1]
    l = [['' for _ in range(N)] for _ in range(M)]
    for (s1, e1), (s2, e2) in zip(solve(), solve()):
        s3, e3 = 2 * s2 - s1, 2 * e2 - e1
        if 0 <= s3 < M and 0 <= e3 < N:
            l[s3][e3] = C
    for line in l:
        print(*line, sep='')
    print()