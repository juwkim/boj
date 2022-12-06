X, Y, N = map(int, input().split())
nums = [*range(1, N+1)]
for i in range(N):
    if nums[i] % X == 0 and nums[i] % Y == 0:
        nums[i] = 'FizzBuzz'
    elif nums[i] % X == 0:
        nums[i] = 'Fizz'
    elif nums[i] % Y == 0:
        nums[i] = 'Buzz'
print(*nums, sep='\n')