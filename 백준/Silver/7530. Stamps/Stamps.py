import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    t, n = g()
    nums = sorted(g(), reverse=True)
    ans = "impossible"
    for i in range(n):
        t -= nums[i]
        if t <= 0:
            ans = i + 1
            break
    print(f"Scenario #{tc}:")
    print(ans)
    print()