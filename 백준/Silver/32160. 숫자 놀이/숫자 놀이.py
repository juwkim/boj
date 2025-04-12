q, r = divmod(N:=int(input()), 4)
print(N - (r > 1))
for i in range((2, 1)[r&1], N, 2):
    print(i, i + 1)
for _ in range(q):
    print(1, 1)
for _ in range(q - 1):
    print(0, 0)
if q and r > 1:
    print(0, 1)
print(+(r > 1), N)