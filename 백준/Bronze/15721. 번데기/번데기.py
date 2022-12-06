A, T, a = map(int, open(0).readlines())
i, s = 4, 0
while T > i:
    T -= i
    s += 2 * i
    i += 1
if T <= 2:
    s += 2 * T + a - 2
else:
    s += T + 1 + a * (i - 2)
print(s % A)