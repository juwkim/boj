import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = []
for l in zip(*[[*map(int, input().split())] for _ in range(N)]):
    nums = sorted(l)
    dist = sum(nums[i] - nums[0] for i in range(1, N))
    pos, distMin = nums[0], dist
    for i in range(1, N):
        dist += (nums[i] - nums[i-1]) * (2*i - N)
        if dist < distMin:
            pos, distMin = nums[i], dist
    ans.append(pos)
print(*ans)