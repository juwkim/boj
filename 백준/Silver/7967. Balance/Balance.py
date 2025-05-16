from functools import lru_cache

n = int(input())
weights = list(map(int, input().split()))

@lru_cache(maxsize=None)
def dfs(used_mask, left, right):
    if used_mask.bit_count() == n:
        return 1
    total = 0
    for i in range(n):
        if used_mask & (1 << i):
            continue
        w = weights[i]
        total += dfs(used_mask | (1 << i), left, right + w)
        if left + w <= right:
            total += dfs(used_mask | (1 << i), left + w, right)
    return total
print(dfs(0, 0, 0))