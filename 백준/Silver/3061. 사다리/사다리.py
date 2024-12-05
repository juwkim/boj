import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = [*map(int, input().split())]
    ans = 0
    for num in range(1, N + 1):
        idx = nums.index(num)
        if idx == num - 1:
            continue
        ans += idx - num + 1
        del nums[idx]
        nums.insert(num - 1, num)
    print(ans)