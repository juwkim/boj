array = []
for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    t = h * 60 + m
    if 390 <= t <= 1140:
        array.append(t)
if array:
    a, b = min(array), max(array)
    if a <= 600:
        if b <= 960:
            v = 24000
        else:
            v = 36000
    else:
        if b > 960:
            v = 24000
        else:
            v = 16800
else:
    v = 0
print(v)