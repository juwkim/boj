g = lambda: [*map(int, input().split())]

A, B = g()
m = int(input())
num = 0
for i in g():
    num = num * A + i
buf = []
while True:
    num, q = divmod(num, B)
    buf.append(q)
    if num == 0:
        break
print(*buf[::-1])