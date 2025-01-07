import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, P = g()
nums = [g() for _ in range(N)]
fuel, cnt = nums[P - 1][0], 1
for i, (A, B) in sorted(enumerate(nums, 1), key=lambda x: x[1][1]):
    if i != P and min(A, fuel) >= B:
        fuel += A - B
        cnt += 1
print(fuel, cnt)