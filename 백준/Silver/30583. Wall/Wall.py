R, K = map(int, input().split())
d = {}
for i in range(8):
    s = "".join("X."[(i & (1 << j)) == 0] for j in range(2, -1, -1))
    if R & (1 << i):
        d[s] = 'X'
    else:
        d[s] = '.'
a = '.' + input() + '.'
for _ in range(K):
    b = ['.'] * len(a)
    for i in range(1, len(a) - 1):
        b[i] = d["".join(a[i - 1:i + 2])]
    print("".join(b[1:-1]))
    a = b