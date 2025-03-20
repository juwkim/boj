T, *Ns = map(int, open(0))
p = [1] * 10000001
for i in range(2, 3163):
    if p[i]:
        for j in range(i * i, 10000001, i): p[j] = 0
a = [0] * 10000001
a[1], a[2] = 1, 1
for i in range(3, 10000001):
    if p[i]: a[i] = a[i - 2] + 1
    else: a[i] = a[i - 1] + 1
for N in Ns: print(a[N])