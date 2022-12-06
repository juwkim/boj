r, q = divmod(int(input()), 3)
if q == 0:
    print(0, r)
elif q == 1:
    print(2, r - 1)
else:
    print(1, r)