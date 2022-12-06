num = int(input()) + 1
buf = [1] * num
for i in range(2, num):
    for j in range(i, num, i):
        buf[j] += i
for i in range(2, num):
    buf[i] += buf[i-1]

print(buf[-1])