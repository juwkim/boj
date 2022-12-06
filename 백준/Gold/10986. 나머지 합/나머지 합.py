g = lambda: [*map(int, input().split())]


from math import comb
N, M = g()
nums = g()
res = [0 for _ in range(M)]
nums[0] %= M
res[nums[0]] += 1
for i in range(1, N):
    nums[i] = (nums[i] + nums[i-1]) % M
    res[nums[i]] += 1

print(res[0] + sum(comb(num, 2) for num in res))