g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    K, P, X = g()
    ans = 1e10
    S = int((K * P / X) ** .5)
    for M in range(S, S + 2):
        D = K / M
        ans = min(ans, D * P + X * M)  


    # for M in range(1, K + 1):
    #     D = K / M
    #     ans = min(ans, D * P + X * M)    
    print("%.3f" % ans)