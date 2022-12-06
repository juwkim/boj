g = lambda: [*map(int, input().split())]

buf = sorted(g() for _ in range(11))
for i in range(10):
    buf[i+1][0] += buf[i][0]
print(sum(buf[i][0] + 20 * buf[i][1] for i in range(11)))