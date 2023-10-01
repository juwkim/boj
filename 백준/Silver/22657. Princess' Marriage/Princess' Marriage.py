import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

while True:
    N, M = g()
    if N == 0:
        break
    nums = sorted([g() for _ in range(N)], key=lambda x: -x[1])
    for i in range(N):
        if nums[i][0] >= M:
            nums[i][0] -= M
            break
        M -= nums[i][0]
        nums[i][0] = 0
    ans = sum([num[0] * num[1] for num in nums])
    print(ans)