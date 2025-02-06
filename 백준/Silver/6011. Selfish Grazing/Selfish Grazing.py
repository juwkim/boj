import sys
input = sys.stdin.readline

N = int(input())
(_, E), *nums = sorted([[*map(int, input().split())] for _ in range(N)], key=lambda x: x[1])
ans = 1
for s, e in nums:
    if E <= s:
        ans += 1
        E = e
print(ans)