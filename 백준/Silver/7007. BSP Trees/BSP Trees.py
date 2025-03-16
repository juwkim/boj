n = int(input())
xP, zP = [0] * n, [0] * n
for i in range(n):
    *_, x, z = map(int, input().split())
    xP[i] = x
    zP[i] = z

p = int(input())
A, B, C = [0] * p, [0] * p, [0] * p

for i in range(p):
    x1, z1, x2, z2 = map(int, input().split())
    A[i] = z1 - z2
    B[i] = x2 - x1
    C[i] = x1 * z2 - z1 * x2
    if B[i] < 0: A[i], B[i], C[i] = -A[i], -B[i], -C[i]

order = list(range(n))
isDiv = bytearray(n + 1)
isDiv[0], isDiv[n] = True, True

for i in range(p):
    pnc = 0
    while pnc < n:
        next_div = pnc + 1
        while not isDiv[next_div]:
            next_div += 1
        
        if next_div == pnc + 1:
            pnc = next_div
            continue
        
        xianNo, houNo = 0, 0
        tempHou = [0] * n
        
        for j in range(next_div - pnc):
            if A[i] * xP[order[pnc + j]] + B[i] * zP[order[pnc + j]] + C[i] > 0:
                order[pnc + xianNo] = order[pnc + j]
                xianNo += 1
            else:
                tempHou[houNo] = order[pnc + j]
                houNo += 1
        
        isDiv[pnc + xianNo] = True
        
        for j in range(houNo):
            order[pnc + xianNo + j] = tempHou[j]
        
        pnc = next_div

print("".join(chr(order[i] + ord('A')) for i in range(n)))