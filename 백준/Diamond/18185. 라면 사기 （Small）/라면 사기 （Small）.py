input = __import__('sys').stdin.readline

N = int(input())
nums = [*map(int, input().split())]

mem = [max(0, nums[1] - nums[0]), min(nums[:2]), 0]
ans = 3 * max(0, nums[0] - nums[1])
for i in range(2, N):

    buf = [0, 0, 0]
    for k in range(2):
        num = min(mem[k], nums[i])
        buf[k + 1] = num
        mem[k] -= num
        nums[i] -= num
    buf[0] = nums[i]

    a, b, c = mem
    ans += 3 * a + 5 * b + 7 * c

    mem = buf
    
a, b, c = mem
ans += 3 * a + 5 * b + 7 * c
print(ans)