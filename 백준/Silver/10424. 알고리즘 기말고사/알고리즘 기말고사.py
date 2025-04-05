N, *nums = map(int, open(0).read().split())
for i, num in sorted(enumerate(nums, 1), key=lambda x: x[1]):
    print(num - i)