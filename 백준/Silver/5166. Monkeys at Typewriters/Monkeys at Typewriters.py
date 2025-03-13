import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    *l, s = input().split()
    n, m = map(int, l)
    s = float(s)
    prob = {}
    for _ in range(m):
        alpha, p = input().split()
        prob[alpha] = float(p)
    ans = 0
    for _ in range(n):
        p = s
        for c in input():
            p *= prob[c]
        ans += p
    print(f"Data Set {tc}:\n{ans:.4E}\n")