import sys
input = lambda: sys.stdin.readline().rstrip()

nums = [int(f"{i}{j}{k}{k}{j}{i}") for i in range(1, 10) for j in range(10) for k in range(10)]
for _ in range(int(input())):
    ans = 1e9
    s = int(input())
    for num in nums:
        if abs(s - num) < abs(s - ans) or (abs(s - num) == abs(s - ans) and num < ans):
            ans = num
    print(ans)