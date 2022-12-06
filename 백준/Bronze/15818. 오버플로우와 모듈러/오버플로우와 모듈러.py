N, M = map(int, input().split())
nums = [*map(int, input().split())]
A = 1
for num in nums:
    A *= num
print(A%M)