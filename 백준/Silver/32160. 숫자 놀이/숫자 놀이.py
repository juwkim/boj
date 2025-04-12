q, r = divmod(N:=int(input()), 4)
if r <= 1:
    print(N)
    for i in range(2 - r, N, 2):
        print(i, i + 1)
    for _ in range(q):
        print(1, 1)
    for _ in range(q - 1):
        print(0, 0)
    print(0, N)
elif r == 2:
    print(N - 1)
    for i in range(2, N, 2):
        print(i, i + 1)
    for _ in range(q):
        print(1, 1)
    for _ in range(q - 1):
        print(0, 0)
    if q:
        print(0, 1)
    print(1, N)
else:
    print(N - 1)
    for i in range(1, N, 2):
        print(i, i + 1)
    for _ in range(q):
        print(1, 1)
    for _ in range(q - 1):
        print(0, 0)
    if q:
        print(0, 1)
    print(1, N)