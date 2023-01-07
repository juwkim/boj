def g(): return [*map(int, input().split())]

for t in range(1, 1 + int(input())):
    
    N, Q = g()
    nums = g()
    px_sum = [0]
    for num in nums:
        px_sum.append(px_sum[-1] + num)

    buf = [0]
    for i in range(N):
        for j in range(i + 1, N + 1):
            buf.append(px_sum[j] - px_sum[i])
    buf.sort()
    
    for i in range(N * (N + 1) // 2):
        buf[i + 1] += buf[i]

    print(f'Case #{t}:')
    for _ in range(Q):
        s, e = g()
        print(buf[e] - buf[s - 1])