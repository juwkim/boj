g = lambda: [*map(int, input().split())]


n, d, k = g()
buf = []
for _ in range(n):
    name, cost = input().split()
    cost = int(cost)
    buf.append([cost, name])
buf.sort(reverse=True)

res = []
idx = 0
while k and d > 0:
    cost, name = buf[idx]
    d -= cost
    k -= 1
    idx += 1
    res.append(name)
if d > 0:
    print('impossible')
else:
    print(len(res))
    for name in res:
        print(f'{name}, YOU ARE FIRED!')