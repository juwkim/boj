A, B, C = [], [], []
for _ in range(3):
    P, Y, S = input().split()
    A.append(int(P))
    B.append(int(Y) % 100)
    C.append(S[0])

print(*sorted(B), sep='')
idx = sorted(range(3), reverse=True, key=lambda i: A[i])
print(*[C[i] for i in idx], sep='')