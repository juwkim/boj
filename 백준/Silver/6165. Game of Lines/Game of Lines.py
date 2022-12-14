from fractions import Fraction
ans, buf, flag = set(), [], False
for _ in range(int(input())):
    p = [*map(int, input().split())]
    for q in buf:
        try:
            ans.add(Fraction(p[0] - q[0], p[1] - q[1]))
        except:
            flag = True
    buf.append(p)
print(len(ans) + flag)