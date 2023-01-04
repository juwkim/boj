def g(): return [*map(int, input().split())]

N = int(input())
ans, t = 1, 1 << N
check = [0] * ((t * t + 2) // 3)
nums = [g() for _ in range(t)]
for i in range(t):
    for j in range(t):
        if nums[i][j] == 0:
            check[0] += 1
            continue

        flag = False
        if i > 0 and j > 0:
            if nums[i][j] == nums[i-1][j] == nums[i][j-1]:
                flag = True
        if i > 0 and j < t - 1:
            if nums[i][j] == nums[i-1][j] == nums[i][j+1]:
                flag = True
        if i < t - 1 and j < t - 1:
            if nums[i][j] == nums[i+1][j] == nums[i][j+1]:
                flag = True
        if i < t - 1 and j > 0:
            if nums[i][j] == nums[i+1][j] == nums[i][j-1]:
                flag = True
        if flag:
            check[nums[i][j]] += 3
if ans:
    if check[0] != 1 or any(check[i] != 3 for i in range(1, (t * t + 2) // 3)):
        ans = 0
print(ans)