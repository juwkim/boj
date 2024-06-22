import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    p, r = map(int, input().split())
    name = [input() for _ in range(p)]
    point, dot = [0] * p, [0] * p
    for _ in range(r):
        cur = [0] * p
        for _ in range(int(input())):
            a, b = map(int, input().split(':'))
            for i in range(p):
                s, t = map(int, input().split(':'))
                if (a, b) == (s, t):
                    cur[i] += 3
                elif (a > b) - (a < b) == (s > t) - (s < t):
                    cur[i] += 1
        m = max(cur)
        for i in range(p):
            point[i] += cur[i]
            dot[i] += cur[i] == m
    print(f"Scenario #{tc}:")
    for i in sorted(range(p), key=lambda x: (-point[x], -dot[x], x)):
        print(point[i], dot[i], name[i])
    print()