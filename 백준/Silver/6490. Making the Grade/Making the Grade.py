import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    S, T = g()
    a = []
    for _ in range(S):
        *scores, bns, abst = g()
        if T > 2: avg = (sum(scores) - min(scores)) / (T - 1)
        else:     avg = sum(scores) / T
        a.append((avg, bns, abst))
    mean = sum(x[0] for x in a) / S
    sd = max(1, (sum((x[0] - mean) ** 2 for x in a) / S) **.5)
    Sum = 0
    for i in range(S):
        AdjAvg = a[i][0] + a[i][1] // 2 * 3
        grade = 1
        if AdjAvg >= mean + sd:   grade = 4
        elif AdjAvg >= mean:      grade = 3
        elif AdjAvg >= mean - sd: grade = 2
        if a[i][2]: grade = max(0, grade - a[i][2] // 4)
        else:       grade = min(4, grade + 1)
        Sum += grade
    print(f"{Sum / S:.1f}")