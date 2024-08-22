import sys
input = sys.stdin.readline

p, q = 0, 0
n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
for color in range(1, 6):
    cnt, l, r = 0, -1, 0
    while r < n:
        if color in nums[r]:
            r += 1
        else:
            cnt = max(cnt, r - l - 1)
            l = r
            r += 1
    cnt = max(cnt, r - l - 1)
    if cnt > p:
        p, q = cnt, color
print(p, q)