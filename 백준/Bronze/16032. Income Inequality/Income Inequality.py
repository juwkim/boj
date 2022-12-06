from statistics import mean
while int(input()):
    nums = [*map(int, input().split())]
    k = mean(nums)
    print(len([*filter(lambda x: x <= k, nums)]))