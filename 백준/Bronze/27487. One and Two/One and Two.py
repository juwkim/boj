def g(): return [*map(int, input().split())]

for _ in range(int(input())):
    n = int(input())
    nums = g()
    left, right = nums[0], nums[-1]
    l, r = 1, n - 2
    while l <= r:
        if left < right:
            left *= nums[l]
            l += 1
        else:
            right *= nums[r]
            r -= 1
    if left == right:
        print(l)
    else:
        print(-1)