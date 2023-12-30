import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N, d, k, c = g()
nums = [int(input()) for _ in range(N)]
check = Counter(nums[-k:])
ans = len(check) + (check[c] == 0)
for i in range(N - 1, -1, -1):
    check[nums[i]] -= 1
    if check[nums[i]] == 0:
        del check[nums[i]]
    check[nums[i - k]] += 1
    ans = max(ans, len(check) + (check[c] == 0))
print(ans)