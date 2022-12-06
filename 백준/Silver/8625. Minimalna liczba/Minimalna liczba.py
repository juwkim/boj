g = lambda: map(int, input().split())

n, k = g()
nums = set(g())

num = k
while num in nums:
    num += k
print(num)