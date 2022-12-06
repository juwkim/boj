time = 0
for _ in range(int(input())):
    h, m = map(int, input().split())
    time += h * 60 + m

m = 1e9
for i in range(time // 240 + 2):
    for j in range(time // 180 + 2):
        if i * 240 + j * 180 >= time:
            m = min(m, 10.9 * i + 9.15 * j)
print('%.2f' % m)