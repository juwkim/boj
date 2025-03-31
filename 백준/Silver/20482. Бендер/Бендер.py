from itertools import product

def solve():
    n, k, r, l = map(int, input().split())
    for a, b, c in product(range(k), repeat=3):
        nums = [*range(k)]
        x = c
        for _ in range(n):
            nums[x], nums[(x + 1) % k] = nums[(x + 1) % k], nums[x]
            x = (a * x + b) % k
        if nums[l - 1] == r - 1:
            return f"{a} {b} {c}"
    return "Impossible"
print(solve())