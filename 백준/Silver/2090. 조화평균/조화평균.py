from math import gcd
_, *nums = map(int, open(0).read().split())
numerator = 1
for num in nums:
    numerator *= num

denominator = 0
for num in nums:
    denominator += numerator // num

GCD = gcd(numerator, denominator)
print("%d/%d" % (numerator // GCD, denominator // GCD))