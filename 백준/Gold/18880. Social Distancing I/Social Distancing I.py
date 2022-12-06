g = lambda: [*map(int, input().split())]

N = int(input())

buf = []
zeros = 0
for cow in input():
    if cow == '1':
        buf.append(zeros)
        zeros = 0
    else:
        zeros += 1


if len(buf) == 0:
    print(N-1)
else:
    s, t = sorted([buf.pop(0), zeros])
    res = [(t - 2) // 2, s - 1]
    buf.sort()
    if len(buf) == 0:
        print(max(res) + 1)
    elif len(buf) == 1:
        b = buf[0]
        res.extend([(b - 2) // 3, min(t-1, (b - 1) // 2)])
        print(min(b, max(res)) + 1)
    else:
        a, b = buf[-2], buf[-1]
        res.extend([(b - 2) // 3, (a - 1) // 2, min(t-1, (b - 1) // 2)])
        print(min(buf[0], max(res)) + 1)