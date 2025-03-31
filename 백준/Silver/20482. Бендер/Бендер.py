from itertools import product

ans = "Impossible"
n, k, r, l = map(int, input().split())
for a, b, c in product(range(k), repeat=3):
    nums = [*range(k)]
    x = c
    for _ in range(n):
        nums[x], nums[(x + 1) % k] = nums[(x + 1) % k], nums[x]
        x = (a * x + b) % k
    if nums[l - 1] == r - 1:
        ans = f"{a} {b} {c}"
        break
print(ans)