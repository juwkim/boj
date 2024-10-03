A, B = map(int, input().split())
L, R = 0, 0
while A and B:
    if A < B:
        q, B = divmod(B, A)
        R += q - (B == 0)
    else:
        q, A = divmod(A, B)
        L += q - (A == 0)
print(L, R)