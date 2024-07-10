f = 1
for i in range(2, int(input()) + 1):
    f *= i
    while f % 10 == 0:
        f //= 10
    f %= 1000000000000
f %= 100000
print(f"{f:05d}")