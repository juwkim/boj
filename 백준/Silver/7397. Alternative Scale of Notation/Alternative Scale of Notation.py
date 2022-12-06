B = int(input())
x = int(input())
buf = []
num = 1
while True:
    if x > num:
        x -= num
        buf.append(1)
    elif x == num:
        x -= num
        buf.append(1)
        break
    else:
        break
    num *= B

idx = -1
while x:
    num //= B
    r, x = divmod(x, num)
    buf[idx] += r
    idx -= 1
    if x == 0:
        break
print(*buf[::-1], sep='')        