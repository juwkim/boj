g = lambda: [*map(int, input().split())]

N = int(input())
nums = [g() for _ in range(3 * N)]
ans = sorted(range(1, 3 * N + 1), key=lambda x: nums[x-1])
for i in range(0, 3 * N, 3):
    print(*ans[i:i+3])