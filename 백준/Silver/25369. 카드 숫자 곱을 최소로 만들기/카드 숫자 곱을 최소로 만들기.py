from itertools import product

n, *A = map(int, open(0).read().split())
if all(num == 9 for num in A):
    print(-1)
else:
    PA = 1
    for num in A:
        PA *= num
    for p in product(range(1, 10), repeat=n):
        PB = 1
        for num in p:
            PB *= num
        if PB > PA:
            print(*p)
            break