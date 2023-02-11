def g(): return [*map(int, input().split())]

for _ in range(int(input())):
    N = int(input())
    nums = [0] * (N // 2) + g()
    for i in range(N // 2, 0, -1):
        tmp = min(nums[2 * i], nums[2 * i - 1])
        nums[2 * i] -= tmp
        nums[2 * i - 1] -= tmp
        nums[i - 1] = tmp
    print(sum(nums))