import sys
input = lambda: sys.stdin.readline().rstrip('\n')
g = lambda: [*map(int, input().split())]

N, M = g()
ans = 'Yes'
for _ in range(M):
    k = int(input())
    nums = g()
    if any(nums[i] < nums[i+1] for i in range(k-1)):
        ans = 'No'
        break
print(ans)