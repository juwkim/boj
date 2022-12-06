g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    N, K = g()
    
    a = pow(2, N) 
    if K >= a - 1 and (K - a + 1) % a == 0:
        ans = 'ON'
    else:
        ans = 'OFF'
    print(f'Case #{_}:', ans)