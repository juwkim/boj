a, b = map(int, input().split())
c, d = map(int, input().split())
bits = []
while (a, b, c, d) != (1, 0, 0, 1):
    if a >= b and c >= d:
        bits.append(0)
        a, c = a - b, c - d
    else:
        bits.append(1)
        b, d = b - a, d - c
print(*bits[::-1], sep='')