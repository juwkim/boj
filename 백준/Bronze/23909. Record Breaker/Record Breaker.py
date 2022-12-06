g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n = int(input())
    Max = -1
    nums = [-1] + g() + [-1]
    ans = 0
    for i in range(1, n+1):
        if nums[i] > Max:
            Max = nums[i]
            if nums[i] > nums[i+1]:
                ans += 1
    print(f'Case #{cnt}: {ans}')