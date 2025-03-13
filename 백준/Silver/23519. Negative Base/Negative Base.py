k = int(input())
if k == 1:
    print(0)
elif k & 1:
    print(-(1 << k))
else:
    print(1 << k)