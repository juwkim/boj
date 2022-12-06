n, m = map(int, input().split())
nums = [int(input()) for _ in range(m)]
check = [0] * m

i = 0
while n and sum(nums):
    if nums[i]:
        check[i] += 1
        nums[i] -= 1
        n -= 1
    i = (i + 1) % m

print(*check)