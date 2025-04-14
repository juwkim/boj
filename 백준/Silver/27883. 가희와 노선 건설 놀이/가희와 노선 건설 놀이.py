n, m, *nums = map(int, open(0).read().split())
print(2 * m + 1)
print(f"U {1} {-1}")
for h, x in enumerate(nums, 1):
    print(f"U {x + 1} {h}")
    print('P')