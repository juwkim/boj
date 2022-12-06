res = []
for _ in range(int(input())):
    name, *l = input().split()
    R, S, D = map(int, l)
    res.append((2 * R + 3 * S + D, name))
res.sort(key=lambda x: (-x[0], x[1]))
for com in res[:2]:
    print(com[1])