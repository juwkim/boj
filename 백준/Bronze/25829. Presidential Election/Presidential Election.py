x, y = 0, 0
a, b = 0, 0
for _ in range(int(input())):
    t, m, n = map(int, input().split())
    x += m
    y += n
    if m > n:
        a += t
    elif m < n:
        b += t
if x > y and a > b:
    print(1)
elif x < y and a < b:
    print(2)
else:
    print(0)