g = lambda: [*map(int, input().split())]

n, m, k = g()
nums = set(range(1, n+1)) - set(g()) - set(g())
print(len(nums))
print(*nums)