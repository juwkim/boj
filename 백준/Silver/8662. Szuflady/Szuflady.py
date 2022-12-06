g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
cnt = 0
Min = nums[N-1]
for i in range(N-2, -1, -1):
    if nums[i] < i + 1:
        cnt = -1
        break
    if nums[i] >= Min:
        cnt += 1
        Min -= 1
    else:
        Min = nums[i]
if nums[N-1] < N:
    cnt = -1
print(cnt)