g = lambda: [*map(int, input().split())]
N, M = g()
buf = []
for _ in range(M):
    a, b, c = input().split()
    buf.append((int(b), int(a), c))
buf.sort()
print(''.join([*zip(*buf)][2]))