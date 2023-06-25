from statistics import mean

for _ in range(int(input())):
    N, *nums = map(int, input().split())
    m = mean(nums)
    ans = sum(num > m for num in nums) * 100 / N + 0.00001
    print(f"{ans:.3f}%")