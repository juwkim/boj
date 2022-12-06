g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted(g())
x = int(input())
ans = 0

l, r = 0, N - 1
while l < r:
    num = nums[l] + nums[r]
    if num == x:
        ans += 1
        l += 1
        r -= 1
    elif num > x:
        r -= 1
    else:
        l += 1
print(ans)