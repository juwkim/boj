N = int(input())
x, y = 1, 1
d = 1
while N:
    x += 1
    N -= 1
    if N <= d:
        y += N
        break
    N -= d
    y += d
    if N <= d:
        x -= N
        break
    N -= d + 1
    x -= d
    y += 1
    d += 1
    if N <= d:
        x += N
        break
    x += d
    N -= d
    if N <= d:
        y -= N
        break
    y -= d
    N -= d
    d += 1
print(x, y)