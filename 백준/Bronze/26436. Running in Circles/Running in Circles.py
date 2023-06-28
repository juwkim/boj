g = lambda: [*map(int, input().split())]

for case in range(1, 1 + int(input())):
    L, N = g()
    ans, prev = 0, 0
    c = 'C'
    for _ in range(N):
        D, C = input().split()
        D = int(D)
        cur = prev + [-D, D][C == 'C']
        
        ans += max(0, abs((cur // L) - (prev // L)) - (c != C and prev % L != 0))
        
        if prev // L != cur // L:
            c = C
        prev = cur

    print(f"Case #{case}: {ans}")