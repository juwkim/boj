g = lambda: [*map(int, input().split())]
N, M = g()
nums = g()

cnt = 0
for _ in range(N-1):
    diff = sum(abs(a - b) for a, b in zip(nums, g()))
    cnt += (diff > 2000)
if cnt >= N // 2:
    print('YES')
else:
    print('NO')