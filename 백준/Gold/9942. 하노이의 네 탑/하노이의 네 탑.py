def T(N):
    if N == 1:
        return 1
    
    K = N - round((2 * N + 1) ** .5) + 1
    return 2 * T(K) + (1 << (N - K)) - 1

i = 1
while True:
    try:
        print(f'Case {i}:', T(int(input())))
        i += 1
    except:
        break