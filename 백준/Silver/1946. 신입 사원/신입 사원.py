import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
for _ in range(int(input())):
    N = int(input())
    nums = [tuple(g()) for _ in range(N)]
    nums.sort()
    ans, s = 1, nums[0][1]
    for i in range(1, N):
        if nums[i][1] < s:
            s = nums[i][1]
            ans += 1
            if s == 1:
                break
    print(ans)