M, N, A, B, X, Y = map(int, open(0).read().split())
if X + M < 0 or X >= A or Y + N < 0 or Y >= B:
    print("NEPATAIKYS")
else:
    xhit = 0
    if X <= 0:
        xhit = 0
    else:
        xhit = X
    if Y <= 0:
        yhit = 0
    else:
        yhit = Y
    print(xhit + yhit)