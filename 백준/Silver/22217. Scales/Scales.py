b = []
m = int(input())
while m:
    m, r = divmod(m, 3)
    b.append(r)
b.append(0)
a = [0] * len(b)
for i in range(len(b) - 1):
    if b[i] == 2:
        b[i] = 0
        b[i + 1] += 1
        a[i] = 1
    elif b[i] == 3:
        b[i] = 0
        b[i + 1] += 1

def solve(l):
    d = 1
    x = []
    for num in l:
        if num:
            x.append(d)
        d *= 3
    return (len(x), *x)
print(*solve(a))
print(*solve(b))