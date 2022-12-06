g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    nums = g()
    nums[8] += nums[5]
    nums[5] = 0
    
    p = sum(nums)
    res = [0] * p
    
    pos = [0, p - 1] 
    idx = 0
    for i in range(8, -1, -1):
        
        while nums[i]:
            
            res[pos[idx]] = i + 1
            if idx == 0:
                pos[idx] += 1
            else:
                pos[idx] -= 1
            idx ^= 1
            nums[i] -= 1  
    print(*res)