g = lambda: [*map(int, input().split())]
while N:= int(input()):
    ans, cnt = 1, 1
    nums = sorted(g())
    for i in range(N - 1):
        if nums[i] + 1 == nums[i + 1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    ans = max(ans, cnt)
    print(ans)