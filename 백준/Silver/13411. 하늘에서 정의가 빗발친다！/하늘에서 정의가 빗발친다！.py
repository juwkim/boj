buf = []
for i in range(1, 1 + int(input())):
    x, y, v = map(int, input().split())
    buf.append(((x ** 2 + y ** 2) / (v ** 2), i))
buf.sort()
print(*[*zip(*buf)][1])