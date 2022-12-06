g = lambda: [*map(int, input().split())]

L, G, R = g()
dic = {}
lamps = [0] * (L + 1)
for _ in range(G):
    name, *l = input().split()
    dic[name] = [*map(int, l)]
for _ in range(R):
    a, d = dic[input()]
    while a <= L:
        lamps[a] ^= 1
        a += d
print(sum(lamps))