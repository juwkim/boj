import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, M, K, X, Y = g()
nums = []
for _ in range(N):
    A, B = g()
    nums.append(A * X - B * Y)
print(K * (X + Y) + sum(sorted(nums)[:M]))