N, *a = map(int, open(0).read().split())
b = bytearray(N + 1)
b[0], b[1] = True, True
for i in range(1, N):
    if a[i] < a[i-1]:
        break
    b[i+1] = True
c = bytearray(N + 1)
c[-1], c[-2] = True, True
for i in range(N - 2, -1, -1):
    if a[i] > a[i+1]:
        break
    c[i] = True
print(sum(b[i] & c[i + 1] & (i in (0, N - 1) or a[i-1] <= a[i+1]) for i in range(N)))