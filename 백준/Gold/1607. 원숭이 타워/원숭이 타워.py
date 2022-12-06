def T(N):
    
    cnt = 0
    i = 1
    while N != 1:
        K = round((2 * N + 1) ** .5) - 1
        cnt += ((1 << K) - 1) * i
        i *= 2
        N -= K
    cnt += i
    
    return cnt

print(T(int(input())) % 9901)