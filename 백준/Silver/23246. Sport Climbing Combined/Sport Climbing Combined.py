g = lambda: [*map(int, input().split())]

buf = []
for _ in range(int(input())):
    num, a, b, c = g()
    buf.append((a*b*c, a+b+c, num))
buf.sort()
res = [buf[i][2] for i in range(3)]
print(*res)  