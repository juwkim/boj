g = lambda: [*map(int, input().split())]

while L := int(input()):
    A = [g() for _ in range(L)]
    B = [g() for _ in range(L)]
    
    ans = 0
    for _ in range(4):
        num = 0
        for i in range(L):
            for j in range(L):
                num += abs(A[i][j] - B[i][j]) <= 100
        ans = max(ans, num)
        A = [l[::-1] for l in zip(*A)]
        
    A = [l[::-1] for l in A]

    for _ in range(4):
        num = 0
        for i in range(L):
            for j in range(L):
                num += abs(A[i][j] - B[i][j]) <= 100
        ans = max(ans, num)
        A = [l[::-1] for l in zip(*A)]

    print("%.2f" % (ans * 100 / (L * L)))