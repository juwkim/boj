for i in range(1, 1 + int(input())):
    N, k = int(input()), 1
    while True:
        S = str(N)
        if all(S[i] <= S[i+1] for i in range(len(S)-1)):
            break
        if int(S[-k]) >= int(S[-k-1]):
            k += 1
        else:
            N -= N%(10**(k-1)) + 1
    print(f'Case #{i}: {N}')