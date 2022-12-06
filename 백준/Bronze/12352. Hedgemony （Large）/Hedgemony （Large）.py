for j in range(1, 1+int(input())):
    N = int(input())
    nums = [*map(int, input().split())]
    for i in range(1, N-1):
        nums[i] = min(nums[i], (nums[i-1] + nums[i+1])/2)
    print(f'Case #{j}: {nums[N-2]}')