import sys
input = sys.stdin.readline
from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())
    d = {}
    for _ in range(n):
        N, p, q, k = input().split()
        d[N] = int(p), int(q), int(k)
    res = defaultdict(lambda: [0, "", 0])
    for _ in range(m):
        _, S, e, arg = input().split()
        if res[S][0]:
            continue
        match e:
            case 'p':
                if res[S][1]:
                    res[S][0] = 1
                else:
                    res[S][1] = arg
                    res[S][2] += d[arg][1]
            case 'r':
                if not res[S][1]:
                    res[S][0] = 1
                else:
                    res[S][2] += d[res[S][1]][2] * int(arg)
                    res[S][1] = ""
            case 'a':
                if not res[S][1]:
                    res[S][0] = 1
                else:
                    res[S][2] += (d[res[S][1]][0] * int(arg) + 99) // 100
    for k in sorted(res):
        print(k, "INCONSISTENT" if res[k][0] or res[k][1] else res[k][2])