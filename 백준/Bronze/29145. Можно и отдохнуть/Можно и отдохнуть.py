g = lambda: [*map(int, input().split())]

n, k = g()
nums = [g() for _ in range(n)]
print(sum(c for a, b, c in nums if k >= a and (k - a) % b == 0))