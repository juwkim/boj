import sys
input = lambda: sys.stdin.readline().rstrip()

nums = [int(f"{i}{j}{k}{k}{j}{i}") for i in range(1, 10) for j in range(10) for k in range(10)]
for _ in range(int(input())):
    ans = 1e9
    s = int(input())
    ans = min(nums, key=lambda x: (abs(s - x), x))
    print(ans)