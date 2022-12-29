N, *nums = map(int, open(0))
flag = 0
for i in range(N - 1):
    if flag:
        if nums[i] <= nums[i+1]: flag = 0
    else:
        if nums[i] >= nums[i+1]: print(i + 1)
        if nums[i] > nums[i+1]: flag = 1
if N == 1 or nums[-2] <= nums[-1]: print(N)