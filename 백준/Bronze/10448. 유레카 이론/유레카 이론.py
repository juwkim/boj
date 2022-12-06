from itertools import combinations_with_replacement as c
nums = [n*(n+1)//2 for n in range(1,46)]

for _ in range(int(input())):
    n, i = int(input()), 0
    while nums[i] < n:
        i += 1
    print(int(n in [*map(sum, c(nums[:i], 3))]))