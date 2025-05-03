import sys
input = sys.stdin.readline

l, m = map(int, input().split())
ans, Min = [], 1e18
for _ in range(m):
    name, *nums = input().split(',')
    p, c, t, r = map(int, nums)
    if 10080 * c * t // (t + r) >= l:
        if p < Min:
            ans, Min = [name], p
        elif p == Min:
            ans.append(name)
if ans:
    print(*ans, sep='\n')
else:
    print("no such mower")