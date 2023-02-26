for _ in range(int(input())):
    n = int(input())
    nums = [0] + [*map(int, input().split())] + [1440]
    cnt = sum((nums[i + 1] - nums[i]) // 120 for i in range(n + 1))
    print(('NO', 'YES')[cnt >= 2])