for _ in range(int(input())):
    D, K, N = map(int, input().split())
    direction = [-N, N][K & 1]
    pos = (K - 1 + direction) % D
    a = (pos + 1 + direction) % D + 1
    b = (pos - 1 + direction) % D + 1    
    print(f'Case #{1+_}:', a, b)