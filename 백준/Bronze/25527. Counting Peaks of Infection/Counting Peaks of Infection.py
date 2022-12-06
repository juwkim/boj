g = lambda: [*map(int, input().split())]

while N:= int(input()):
    nums = g()
    cnt = 0
    for i in range(1, N-1):
        cnt += nums[i] > nums[i-1] and nums[i] > nums[i+1]
    
    print(cnt)