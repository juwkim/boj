g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()

ans, cnt = 1, 1
dec = True
for i in range(N-1):
    if nums[i] < nums[i+1]:
        if dec:
            dec = False
            ans = max(ans, cnt)
            cnt = 2
        else:
            cnt += 1
    elif nums[i] > nums[i+1]:
        dec = True
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
ans = max(ans, cnt)
print(ans)