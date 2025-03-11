import sys
input = sys.stdin.readline
for tc in range(1, 1 + int(input())):
    n = int(input())
    nums = [[*map(int, input().split())] for _ in range(n)]
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            a, b = nums[i]
            c, d = nums[j]
            ans = max(ans, abs(a - c) - abs(b - d))
    print(f"Case #{tc}: {ans / 2:.9f}")