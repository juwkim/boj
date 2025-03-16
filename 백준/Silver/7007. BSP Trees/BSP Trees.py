n = int(input())
xC, zC = [0] * n, [0] * n
for i in range(n): *_, x, z = map(int, input().split()); xC[i], zC[i] = x, z

p = int(input())
A, B, C = [0] * p, [0] * p, [0] * p
for i in range(p):
    x1, z1, x2, z2 = map(int, input().split())
    A[i], B[i], C[i] = z1 - z2, x2 - x1, x1 * z2 - z1 * x2
    if B[i] < 0: A[i], B[i], C[i] = -A[i], -B[i], -C[i]

order = list(range(n))
isD = bytearray(n + 1)
isD[0], isD[n] = 1, 1

for i in range(p):
    idx = 0
    while idx < n:
        nxt = idx + 1
        while not isD[nxt]: nxt += 1
        if nxt == idx + 1: idx = nxt; continue
        
        fCnt, bCnt, tmpB = 0, 0, [0] * n
        for j in range(nxt - idx):
            if A[i] * xC[order[idx + j]] + B[i] * zC[order[idx + j]] + C[i] > 0:
                order[idx + fCnt] = order[idx + j]; fCnt += 1
            else:
                tmpB[bCnt] = order[idx + j]; bCnt += 1
        
        isD[idx + fCnt] = 1
        for j in range(bCnt): order[idx + fCnt + j] = tmpB[j]
        idx = nxt

print("".join(chr(order[i] + 65) for i in range(n)))