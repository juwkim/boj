n, m = map(int, [input(), input()])
max_car = 0
for _ in range(n):
    a, b = map(int, input().split())
    m += a - b
    if m < 0:
        max_car = 0
        break
    if m > max_car:
        max_car = m
print(max_car)