import sys
input = sys.stdin.readline

while N:=int(input()):
    nums = [int(input()) for _ in range(N)]
    if all(num <= 0 for num in nums):
        ans = max(nums)
    else:
        ans, cur = 0, 0
        for num in nums:
            cur = max(0, cur + num)
            ans = max(ans, cur)
    print(ans)