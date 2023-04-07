g = lambda: [*map(int, input().split())]

buf = bytearray(86400)
for _ in range(sum(g())):
    h, m, s = map(int, input().split(':'))
    t = h * 3600 + m * 60 + s
    for i in range(t, t + 40):
        buf[i] = 1
print(86400 - sum(buf))