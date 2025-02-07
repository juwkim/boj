import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while (l := g()) != [0, 0]:
    N, M = l
    check = [bytearray(1260) for _ in range(M + 1)]
    recode = {}
    for _ in range(int(input())):
        t, n, m, s = g()
        if s:
            recode[(n, m)] = t
        else:
            check[m][recode[(n, m)]:t] = [1] * (t - recode[(n, m)])
    for _ in range(int(input())):
        s, e, m = g()
        print(sum(check[m][s:e]))