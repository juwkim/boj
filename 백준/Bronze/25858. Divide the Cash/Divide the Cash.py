n, t = map(int, input().split())
nums = [int(input()) for _ in range(n)]
a = t // sum(nums)
for num in nums:
    print(a * num)