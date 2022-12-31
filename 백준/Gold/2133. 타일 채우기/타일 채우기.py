q, r = divmod(int(input()), 2)
if r:
    a = 0
else:
    a, b, c = 1, 3, 11
    for _ in range(q):
        a, b, c = b, c, c * 4 - b
print(a)