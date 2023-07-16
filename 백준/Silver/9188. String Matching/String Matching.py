from fractions import Fraction
while (s:= input()) != "-1":
    a, b = s.split()
    ans = 0
    for i in range(len(a)):
        cur = sum(p == q for p, q in zip(a[i:], b))
        ans = max(ans, cur)
    for i in range(len(b)):
        cur = sum(p == q for p, q in zip(a, b[i:]))
        ans = max(ans, cur)
    print(f"appx({a},{b}) = {Fraction(ans * 2, len(a) + len(b))}")