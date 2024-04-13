from fractions import Fraction

for l in map(str.rstrip, open(0)):
    num, b = Fraction(), 8
    for c in l[2:]:
        num += Fraction(int(c), b)
        b <<= 3
    ans = ["0."]
    while num:
        q, num = divmod(num * 10, 1)
        ans.append(str(q))
    print(f"{l} [8] = {''.join(ans)} [10]")