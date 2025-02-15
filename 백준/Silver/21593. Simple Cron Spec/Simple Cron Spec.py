import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(p):
    i, s = p
    if s == '*':
        if i == 0:
            return list(range(24))
        return list(range(60))
    l = []
    for x in s.split(','):
        if '-' in x:
            a, b = map(int, x.split('-'))
            l.extend(range(a, b + 1))
        else:
            l.append(int(x))
    return l

a, b = bytearray(24 * 60 * 60), 0
for _ in range(int(input())):
    hh, mm, ss = map(solve, enumerate(input().split()))
    b += len(hh) * len(mm) * len(ss)
    for h in hh:
        for m in mm:
            for s in ss:
                a[h * 3600 + m * 60 + s] = 1
print(a.count(1), b)