while True:
    try:
        N, K = map(int, input().split())
        isprime = [True] * (N + 1)
        for i in range(2, N + 1):
            if isprime[i]:
                K -= 1
                if K == 0:
                    print(i)
                    break
                for j in range(2 * i, N + 1, i):
                    if isprime[j]:
                        isprime[j] = False
                        K -= 1
                        if K == 0:
                            print(j)
                            break
                else:
                    continue
                break
    except:
        break