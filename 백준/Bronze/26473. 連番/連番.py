while N:= int(input()):
    ans, cnt = 1, 1
    nums = sorted(map(int, input().split()))
    for i in range(N - 1):
        if nums[i] + 1 == nums[i + 1]:
            cnt += 1
        else:
            ans, cnt = max(ans, cnt), 1
    print(max(ans, cnt))