for i in range(int(input())):
    N, K = map(int, input().split())
    S = input()
    a = sum(S[i] != S[N-1-i] for i in range(N//2))
    print(f'Case #{i+1}: {abs(K - a)}')