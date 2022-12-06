n = int(input())
max_buf = []
for i in range(1, n+1):
    buf = [n, i]
    while buf[-1] >= 0:
        buf.append(buf[-2] - buf[-1])
    if len(buf) > len(max_buf):
        max_buf = buf
print(len(max_buf) - 1)
print(*max_buf[:-1])