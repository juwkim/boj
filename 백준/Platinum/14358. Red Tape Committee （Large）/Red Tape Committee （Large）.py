for t in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    P = sorted(map(float, input().split()))
    
    ans = 0
    for M in range(K + 1):

        dp = [1]
        for p in P[:M] + P[N + M - K:]:
            
            buf = [0] * (min(len(dp), K // 2) + 1)
            for idx, num in enumerate(dp):
                buf[idx] += num * (1 - p)
                if idx + 1 == K // 2 + 1:
                    break
                buf[idx + 1] += num * p
            dp = buf

        ans = max(ans, dp[-1])

    print(f'Case #{t}: {ans}')