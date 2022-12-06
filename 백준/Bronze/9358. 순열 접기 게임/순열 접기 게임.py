for i in range(1, 1 + int(input())):
    N = int(input())
    nums = [*map(int, input().split())]
    while N != 2:
        for j in range(-(-N//2)):
            nums[j] += nums[N - 1 - j]
        N = -(-N//2)
    print(f'Case #{i}: {["Bob", "Alice"][nums[0] > nums[1]]}')