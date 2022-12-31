q, r = divmod(int(input()), 2)
if r:
    a = 0
else:
    a, b = 1, 3 
    for _ in range(q):
        a, b = b, b * 4 - a
print(a)