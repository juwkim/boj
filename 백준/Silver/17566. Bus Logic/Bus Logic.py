g = lambda: [*map(int, input().split())]

m, b, s = g()
buf = [0] * s
for _ in range(b):
    tmp = input()
    if tmp[m-1] == '1':
        for i in range(s):
            if tmp[i] == '1':
                buf[i] = 1
buf[m-1] = 0
print(sum(buf))