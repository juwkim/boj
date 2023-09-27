import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, m = g()
    buf = [['b'] * (m + 2)] + [['b'] + list(input()) + ['b'] for _ in range(n)] + [['b'] * (m + 2)]
    ans = "Well done Clark!"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if buf[i][j] == 'F':
                p = sum(buf[s][t] in 'Fb' for s in range(i - 1, i + 2) for t in range(j - 1, j + 2))
                if p == 9:
                    ans = "Please sweep the mine again!"
                    break
            else:
                p = sum(buf[s][t] == 'F' for s in range(i - 1, i + 2) for t in range(j - 1, j + 2))
                if p != int(buf[i][j]):
                    ans = "Please sweep the mine again!"
                    break
        else:
            continue
        break
    print(ans)
