n = int(input())
nums = input().split()
if any(set(nums[i:i+3]) == set([*'012']) for i in range(n-2)):
    print('TAK')
else:
    print('NIE')