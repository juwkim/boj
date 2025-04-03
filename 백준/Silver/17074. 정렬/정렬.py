N, *a = map(int, open(0).read().split())
b = bytearray(N)
b[0] = True
for i in range(1, N):
    if a[i] < a[i-1]:
        break
    b[i] = True
c = bytearray(N)
c[-1] = True
for i in range(N - 2, -1, -1):
    if a[i] > a[i+1]:
        break
    c[i] = True
ans = 0
for i in range(N):
    if i == 0:
        ans += c[1]
    elif i == N - 1:
        ans += b[N - 2]
    else:
        ans += b[i - 1] & c[i + 1] & (a[i-1] <= a[i+1])
print(ans)