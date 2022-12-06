for _ in range(int(input())):
    M, N = map(int, input().split())
    nums = [[*map(int, input().split())] for _ in range(N)]
    
    res = []
    for j in range(M):
        a = 1
        for i in range(N):
            a *= nums[i][j]
        res.append(a)
    print(1 + max(i for i in range(M) if res[i] == max(res)))