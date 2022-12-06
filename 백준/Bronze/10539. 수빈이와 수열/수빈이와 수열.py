n = int(input())
nums = [*map(int, input().split())]
start = 0
for i in range(n):
    print((i+1)*nums[i] - i*start, end=' ')
    start = nums[i]