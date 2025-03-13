import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    n, m, k = g()
    nums = [set() for _ in range(m)]
    for _ in range(k):
        r, s = g()
        nums[s - 1].add(r)
    ans = 0
    for l in nums:
        cnt, prv = 0, -1
        for num in sorted(l):
            if num == prv + 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            prv = num
        ans = max(ans, cnt)
    if ans == 1:
        ans = 0
    print(ans)