import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

hh, mm = map(int, input().split(':'))
t = hh * 60 + mm
h = g()
for _ in range(int(input())):
    _, e = input().split()
    if e == '^':
        h[t // 120 % 6] = 0
    elif e[-1] == 'N':
        t += int(e[:2])
    else:
        t += int(e[0]) * 60
print(min(100, sum(h)))