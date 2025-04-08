L, *nums = map(int, open(0).read().split())
a, b = 0, 0
for d in range(1, L + 1):
    num = sum(nums[d-1::d])
    if num > b:
        a, b = d, num
print(a, b)