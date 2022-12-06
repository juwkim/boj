temp = []

for _ in range(3):
    a, b, c, d = map(int, input().split())
    x, y = sorted([a * 10 + b, c * 10 + d])
    temp.append([x, y])

p, q = temp[0]
a = temp[1][0] - p >= 10 and temp[1][1] >= q
b = temp[2][0] - p >= 10 and temp[2][1] >= q
if a and b:
    if temp[1][0] > temp[2][0]:
        v = 2
    else:
        v = 1
elif a:
    v = 1
elif b:
    v = 2
else:
    v = 0

print(v)
if v:
    print(temp[v][0] / 10, temp[v][1] / 10)