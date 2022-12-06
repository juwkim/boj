def check(i):
    r1, c1, w1, h1 = l
    for j in range(i):
        r2, c2, w2, h2 = buf[j]
        a = (r1 <= r2 < r1 + h1) or (r1 < r2 + h2 <= r1 + h1) or (r2 < r1 < r1 + h1 < r2 + h2)
        b = (c1 <= c2 < c1 + w1) or (c1 < c2 + w2 <= c1 + w1) or (c2 < c1 < c1 + w1 < c2 + w2)
        if a and b:
            ans[j] = 1
            ans[i] = 1

while n := int(input()):
    buf = []
    ans = bytearray(n)
    for i in range(n):
        l = [*map(int, input().split())]
        check(i)
        buf.append(l)
    print(sum(ans))