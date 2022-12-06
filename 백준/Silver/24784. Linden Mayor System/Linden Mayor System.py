g = lambda: [*map(int, input().split())]

n, m = g()
dic = {}
for _ in range(n):
    x, y = input().split(' -> ')
    dic[x] = y
s = input()
for _ in range(m):
    buf = []
    for c in s:
        if c in dic:
            buf.append(dic[c])
        else:
            buf.append(c)
    s = ''.join(buf)
print(s)