N, *b = map(int, open(0).read().split())
a, sum = [0] * N, 0
for i in range(N):
    if i * (b[i] + 1) < sum:
        a[i] = b[i] + 1
    elif i * b[i] >= sum:
        a[i] = b[i]
    if a[i] == 0:
        print(-1)
        break
    sum += a[i]
else:
    print(*a)