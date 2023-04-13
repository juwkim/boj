for _ in range(int(input())):
    N, K = map(int, input().split())
    
    a = (N + K) // (K + 1)
    print(N - a)