import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

n = int(input())
ans, nums = zip(*sorted(enumerate(g(), 1), key=lambda x: x[1], reverse=True))
if nums[0] > sum(nums[1:]):
    print("impossible")
else:
    print(*ans)