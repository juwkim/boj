for _ in range(int(input())):
    K, N = map(int, input().split())
    print(K, N*(N+1)//2, N**2, N*(N+1))