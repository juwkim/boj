from math import inf

N, K, *A = map(int, open(0).read().split())

def pstdev(i, j):
    n = j - i + 1
    return ((EX2[j + 1] - EX2[i]) * n - ((EX[j + 1] - EX[i])) ** 2) **.5 / n

EX2, EX = [0], [0]
for a in A:
    EX2.append(EX2[-1] + a ** 2)
    EX.append(EX[-1] + a)

ans = inf
for i in range(N - K + 1):
    for j in range(i + K - 1, N):
        ans = min(ans, pstdev(i, j))
print(ans)