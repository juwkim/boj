for cnt in range(1, 1 + int(input())):
    S, K = input().split()
    K = int(K)
    ans = 0
    
    buf = [i == '-' for i in S]
    for i in range(len(S)-K+1):
        if buf[i]:
            for j in range(i, i+K):
                buf[j] ^= 1
            ans += 1
    if sum(buf[-K+1:]):
        ans = 'IMPOSSIBLE'
    print(f'Case #{cnt}: {ans}')