from fractions import Fraction

while (s:=input()) != '#':
    i = len(s) - 1
    if s[-1] == 'h':
        a = Fraction(0)
        i -= 5
    else:
        a = Fraction(90)
        i -= 4
    d = Fraction(45)
    while i >= 0:
        if s[i] == 'h':
            a -= d
            i -= 5
        else:
            a += d
            i -= 4
        d /= 2
    print(a)