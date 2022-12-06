g = lambda: [*map(int, input().split())]
 
N, K, R = g()
nums = bytearray(N+1)
for _ in range(K):
    nums[int(input())] = 1
 
ans = 0
cur = sum(nums[1:R])
for i in range(R, N+1):
    cur += nums[i]
    if cur == 0:
        ans += 2
        cur = 2
        
        j = i
        while nums[j]:
            j -= 1
        nums[j] = 1
        
        while nums[j]:
            j -= 1
        nums[j] = 1
        
    elif cur == 1:
        ans += 1
        cur = 2
        
        j = i
        while nums[j]:
            j -= 1
        nums[j] = 1
    cur -= nums[i-R+1]

print(ans)