input = __import__('sys').stdin.readline
g = lambda: [*map(int, input().split())]

N, B, C = g()
nums = g()
if B > C:
    mem = [max(0, nums[1] - nums[0]), min(nums[:2]), 0]
    ans = B * max(0, nums[0] - nums[1])
    for i in range(2, N):
    
        buf = [0, 0, 0]
        for k in range(2):
            num = min(mem[k], nums[i])
            buf[k + 1] = num
            mem[k] -= num
            nums[i] -= num

        a, b, c = mem
        ans += B * a + (B + C) * b + (B + 2 * C) * c
        
        buf[0] = nums[i]
        mem = buf
        
    a, b, c = mem
    ans += B * a + (B + C) * b + (B + 2 * C) * c
else:
    ans = B * sum(nums)
print(ans)