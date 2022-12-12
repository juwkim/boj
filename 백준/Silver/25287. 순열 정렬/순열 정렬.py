for _ in range(int(input())):
    N = int(input())
    nums = [*map(int, input().split())]
    ans = 'YES'
    if nums[0] > N + 1 - nums[0]:
        nums[0] = N + 1 - nums[0]
        
    for i in range(N - 1):
        if nums[i] <= N + 1 - nums[i+1] <= nums[i+1]:
            nums[i+1] = N + 1 - nums[i+1]                             
        if nums[i] > nums[i + 1]:
            nums[i+1] = N + 1 - nums[i+1]
        if nums[i] > nums[i + 1]:
            ans = 'NO'
            break
    print(ans)