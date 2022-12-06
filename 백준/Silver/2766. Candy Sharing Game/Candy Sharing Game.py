while N := int(input()):
    nums = [int(input()) for _ in range(N)]
    i = 0
    while len(set(nums)) != 1:
        i += 1
        buf = [0] * N
        for j in range(N):
            buf[j] = nums[j] // 2 + nums[j-1] // 2
            if buf[j]&1:
                buf[j] += 1
        nums = buf    
    print(i, nums[0])