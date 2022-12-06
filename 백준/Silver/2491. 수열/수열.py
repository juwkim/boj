g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = 1
cur_incre, cur_decre = 1, 1
for i in range(1, N):
    if nums[i] > nums[i-1]:
        cur_incre += 1
        cur_decre = 1
        ans = max(ans, cur_incre)
    elif nums[i] < nums[i-1]:
        cur_incre = 1
        cur_decre += 1
        ans = max(ans, cur_decre)
    else:
        cur_incre += 1
        cur_decre += 1
        ans = max(ans, cur_incre, cur_decre)
print(ans)