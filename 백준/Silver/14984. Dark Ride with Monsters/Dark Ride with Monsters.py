while True:
    try:
        N = int(input())
        nums = [*map(int, input().split())]
        idxs = [0] * (N + 1)
        for idx, num in enumerate(nums, 1):
            idxs[num] = idx

        ans = 0            
        for idx, num in enumerate(nums, 1):
            if idx == num:
                continue
            ans += 1
            nums[idxs[idx] - 1] = num
            idxs[num] = idxs[idx]
        print(ans)
    except:
        break