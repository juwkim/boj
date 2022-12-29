g = lambda: [*map(int, input().split())]

N, D = g()
nums = g()
ans, cur = 0, 0
while cur < N - 1:
    flag = False
    for idx in range(cur + 1, min(N, cur + D + 1)):
        if nums[idx]:
            cur = idx
            flag = True
            break
    if flag == False:
        cur += D
        ans += 1
print(ans)