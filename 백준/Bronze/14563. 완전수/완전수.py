input()
nums = [*map(int, input().split())]
for num in nums:
    fac = sum(i for i in range(1, num) if num % i == 0)
    print(["Perfect", "Abundant", "Deficient"][(fac > num) - (fac < num)])