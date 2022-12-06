g = lambda: [*map(int, input().split())]

for i in range(1, 1 + int(input())):
    s, t = g()
    buf = [0] * (s + 1)
    for _ in range(t):
        a, b = g()
        buf[a] += b
    idx = buf.index(max(buf))
    print(f'Data Set {i}:')
    if all(buf[idx] > 2 * buf[i] for i in range(1, s+1) if i != idx):
        print(f'{idx}\n')
    else:
        print('No suspect.\n')