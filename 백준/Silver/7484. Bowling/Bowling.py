for _ in range(int(input())):
    ans = 0
    idx, cnt = 0, 0
    nums = [*map(int, input().split())]
    while cnt != 10:
        if nums[idx] == 10:
            ans += nums[idx] + nums[idx+1] + nums[idx+2]
            idx += 1
            cnt += 1
        elif nums[idx] + nums[idx+1] == 10:
            ans += nums[idx] + nums[idx+1] + nums[idx+2]
            idx += 2
            cnt += 1
        else:
            ans += nums[idx] + nums[idx+1]
            idx += 2
            cnt += 1
    print(ans)