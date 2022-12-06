import sys
nums = [*map(int, sys.stdin.read().split()[:-1])]
for num in nums:
    t = sum(i for i in range(1, num) if num % i == 0)
    print(num, 'PERFECT' if t == num else 'ABUNDANT' if t > num else 'DEFICIENT')