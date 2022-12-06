g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    N = int(input())
    nums = g()
    ans = 0
    for i in range(N - 1):
        j = nums.index(min(nums[i:]))
        nums[i:j+1] = nums[i:j+1][::-1]
        ans += j - i + 1
    print(f'Case #{cnt}: {ans}')