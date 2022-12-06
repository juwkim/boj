g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    L = int(input())
    nums = g()
    ans = 0
    for i in range(L-1):
        for j in range(L-1-i):
            if nums[j] > nums[j+1]:
                ans += 1
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(f'Optimal train swapping takes {ans} swaps.')