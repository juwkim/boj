A, B = map(int, input().split())
L, R = 0, 0
while A != B:
    if A < B:
        R += 1
        B -= A
    else:
        L += 1
        A -= B
print(L, R)