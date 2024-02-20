from itertools import product

m = int(input())
l = 0
num = 1
while num * 2 < m:
    num *= 2
    l += 1

buf = [*product('01', repeat=l)]
t = m - num
for i in range(len(buf) - t):
    print(*buf[i], sep='')
for i in range(len(buf) - t, len(buf)):
    s = "".join(buf[i])
    print(s, '0', sep='')
    print(s, '1', sep='')