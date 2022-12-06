for i in range(1, 1 + int(input())):
    n, A, B, C, D, x0, y0, M = map(int, input().split())
    nums = [[0] * 3 for _ in range(3)]
    X, Y = x0, y0
    for _ in range(n):
        nums[X % 3][Y % 3] += 1
        X, Y = (A * X + B) % M, (C * Y + D) % M

    ans = 0
    for line in zip(*nums):
        ans += line[0] * line[1] * line[2]
    for line in nums:
        ans += line[0] * line[1] * line[2]
        for num in line:
            ans += num * (num - 1) * (num - 2) // 6
    ans += nums[0][0] * (nums[1][1] * nums[2][2] + nums[1][2] * nums[2][1])
    ans += nums[0][1] * (nums[1][0] * nums[2][2] + nums[1][2] * nums[2][0])
    ans += nums[0][2] * (nums[1][0] * nums[2][1] + nums[1][1] * nums[2][0])
    print(f'Case #{i}: {ans}')