g = lambda: [*map(int, input().split())]

flag = False
N = int(input())
nums = [list(i) for i in input().split()]

for i in range(N-1):
    if len(nums[i]) == len(nums[i+1]):
        for j in range(len(nums[i])):
            tmp = nums[i][j]
            nums[i][j] = '98'[tmp == '9']
            if int(''.join(nums[i])) > int(''.join(nums[i+1])):
                flag = True
                break
            nums[i][j] = tmp
        
        if flag:
            break
        
        for j in range(len(nums[i+1])):
            tmp = nums[i+1][j]
            if len(nums[i+1]) == 1 or j != 0:
                nums[i+1][j] = '01'[tmp == '0']
            else:
                nums[i+1][j] = '12'[tmp == '1']
            if int(''.join(nums[i])) > int(''.join(nums[i+1])):
                flag = True
                break
            nums[i+1][j] = tmp
        
        if flag:
            break
    if flag:
        break
if flag:
    for num in nums:
        print(''.join(num), end=' ')
else:
    print('impossible')