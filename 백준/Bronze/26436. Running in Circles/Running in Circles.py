for case in range(1, 1 + int(input())):
    L, N = map(int, input().split())
    ans, pos = 0, 0
    direction = 'C'
    for _ in range(N):
        D, C = input().split()
        D = int(D)
        
        if C == direction:
            cycle, pos = divmod(pos + D, L)
        else:
            cycle, pos = divmod(-pos + D, L)
            if cycle != -1:
                direction = C
        ans += cycle
    print(f"Case #{case}: {ans}")