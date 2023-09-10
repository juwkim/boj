import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, C, H = g()
cube = [["." * (C + 2)] + ["." + input() + "." for _ in range(R)] + ["." * (C + 2)] for _ in range(H)]
cube = [["." * (C + 2) for _ in range(R + 2)]] + cube + [["." * (C + 2) for _ in range(R + 2)]]

for i in range(1, H + 1):
    for j in range(1, R + 1):
        tmp = []
        for k in range(1, C + 1):
            if cube[i][j][k] == '*':
                tmp.append('*')
                continue
            num = 0
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    for r in range(k - 1, k + 2):
                        num += cube[p][q][r] == '*'
            tmp.append(num % 10)
        print(*tmp, sep='')