from itertools import combinations
M, N = map(int, input().split())
buf = []
for _ in range(M):
    nums = [*map(int, input().split())]
    a = [sum(num <= i for i in nums) for num in nums]
    buf.append(a)
print(sum(i == j for i, j in combinations(buf, 2)))