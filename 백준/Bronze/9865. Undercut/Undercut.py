for r in range(1, 1 + int(input())):
    m = int(input())
    nums = [*map(int, input().split())]
    while len(nums) != 2 * m:
        nums.extend(map(int, input().split()))
    tessa, danny = 0, 0
    for i in range(0, 2 * m, 2):
        a, b = nums[i], nums[i + 1]
        if a == 1:
            if b == 2:
                tessa += 6
            elif b > 2:
                danny += b
        elif b == 1:
            if a == 2:
                danny += 6
            elif a > 2:
                tessa += a
        elif a == b + 1:
            danny += a + b
        elif b == a + 1:
            tessa += a + b
        elif a > b:
            tessa += a
        elif b > a:
            danny += b
    print(f'Game {r}: Tessa {tessa} Danny {danny}')