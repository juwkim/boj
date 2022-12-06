N, X = map(int, input().split())
nums = [*map(int, input().split())]

idx = 0
while nums[idx % N] >= X:
    X += 1
    idx += 1
print(idx % N + 1)