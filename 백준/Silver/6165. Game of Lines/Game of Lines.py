g = lambda: [*map(int, input().split())]

from fractions import Fraction
ans = set()
buf = []
flag = False
for _ in range(int(input())):
    p = g()
    for q in buf:
        try:
            ans.add(Fraction(p[0] - q[0], p[1] - q[1]))
        except:
            flag = True
    buf.append(p)
print(len(ans) + flag)