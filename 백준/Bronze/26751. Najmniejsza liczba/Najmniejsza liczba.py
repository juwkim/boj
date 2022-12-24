X, Y, Z = sorted(map(int, input().split()))
if X:
    print(X, Y, Z, sep='')
elif Y:
    print(Y, X, Z, sep='')
else:
    print(Z, X, Y, sep='')