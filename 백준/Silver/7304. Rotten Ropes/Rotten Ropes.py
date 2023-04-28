for _ in range(int(input())):
    N = int(input())
    nums = sorted(map(int, input().split()), reverse=True)
    
    ans = 0
    for i in range(N):
        ans = max(ans, (i + 1) * nums[i])
    print(ans)