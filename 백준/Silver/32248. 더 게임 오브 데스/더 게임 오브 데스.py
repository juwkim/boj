N, T, *A = map(int, open(0).read().split())
x = 0
idx = {x: 0}
log = [x]
for i in range(1, T + 1):
    x = A[x] - 1
    if x in idx:
        loop = len(log) - idx[x]
        x = log[(T - idx[x]) % loop + idx[x]]
        break
    log.append(x)
    idx[x] = i
print(x + 1)