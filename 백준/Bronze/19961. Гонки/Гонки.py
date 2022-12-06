g = lambda: [*map(int, input().split())]

t1, v1, t2, v2 = g()
x = int(input())

r1, q1 = divmod(x, v1 * t1)
r2, q2 = divmod(x, v2 * t2)
if r1 and q1:
    first = 2 * r1 * t1 + q1 / v1
elif r1:
    first = (2 * r1 - 1) * t1
else:
    first = q1 / v1

if r2 and q2:
    second = 2 * r2 * t2 + q2 / v2
elif r2:
    second = (2 * r2 - 1) * t2
else:
    second = q2 / v2

print(['Draw', 'First', 'Second'][(first < second) - (first > second)])