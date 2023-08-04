buf = []
for _ in range(9):
    name, a, b = input().split()
    buf.append([name, int(a), int(b)])

for i in range(9):
    s, t = map(int, input().split())
    buf[i][1] += s
    buf[i][2] += t

num = max(range(9), key=lambda x: buf[x][1] / buf[x][2])
if num == 3:
    pass
elif num < 3:
    tmp = buf[num]
    buf[num] = buf[3]
    buf[3] = tmp
else:
    buf.insert(3, buf[num])
    del buf[num + 1]

for i in range(9):
    print(buf[i][0])