n, a = map(int, input().split())

i = 1 << n - 1
while i and (a & i) == 0:
    i >>= 1

j = 1 << n - 1
while j and (a & j):
    j >>= 1
print(a & ~i if i else 0, a | j if j else a)