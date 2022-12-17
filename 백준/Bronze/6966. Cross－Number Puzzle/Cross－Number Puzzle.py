buf = []
for i in range(1000, 10000):
    a = sum(j for j in range(1, i) if i % j == 0)
    if a == i:
        buf.append(i)
print(*buf)
buf = []
for i in range(100, 1000):
    a = sum(int(j) ** 3 for j in str(i))
    if i == a:
        buf.append(i)
print(*buf)