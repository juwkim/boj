import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    n, m, p, y = g()
    time = [0] + g()
    a = [0] + g()
    person = [(0, 0)] + [g() for _ in range(p)]
    bus = [(0, 0)] * (m + 1)
    ans, id = 0, 1
    for i in range(1, n):
        for j in range(1, m + 1):
            if bus[j][1] == i:
                bus[j] = (0, 0)
        while id <= p and person[id][0] == i:
            _, t = person[id]
            l = [j for j in range(1, m + 1) if bus[j] == (0, 0)]
            if l:
                idx = max(l, key=lambda x: a[x])
                bus[idx] = (id, t)
            id += 1
        cur, yin = 0, -1
        for j in range(1, m + 1):
            if bus[j][0]:
                cur += a[j]
            if bus[j][0] == y:
                yin = j
        if yin != -1:
            ans += time[i] * a[yin] / cur
    print(f"Data Set {tc}:\n{ans:.2f}\n")