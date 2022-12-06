def g(num, base):
    s = 0
    while num:
        s += num%base
        num //=base
    return s

for i in range(2992, 9999):
    if g(i, 10) == g(i, 12) == g(i, 16):
        print(i)