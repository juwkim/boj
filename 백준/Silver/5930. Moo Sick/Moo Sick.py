N = int(input())
A = [int(input()) for _ in range(N)]
C = int(input())
B = sorted(int(input()) for _ in range(C))
for i in range(C - 1, -1, -1):
    B[i] -= B[0]

res = []
for i in range(N - C + 1):
    P = sorted(A[i:i + C])
    res.append(all(P[i] - P[0] == B[i] for i in range(C)))

print(sum(res))
for i in range(N - C + 1):
    if res[i]:
        print(i + 1)