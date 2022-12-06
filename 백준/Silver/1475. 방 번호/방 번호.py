buf = [0] * 10
for i in input():
    buf[int(i)] += 1
a = (buf[6] + buf[9] + 1) // 2
buf[6] = a
buf[9] = a

print(max(buf))