t, *nums = map(int, open(0).read().split())
for n in nums:
    print(n * (n - 1) >> 1)