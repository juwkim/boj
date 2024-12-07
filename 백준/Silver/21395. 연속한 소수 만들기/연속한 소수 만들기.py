import sys
input = sys.stdin.readline

def seive(n):
    nums = [True] * (n + 1)
    nums[0], nums[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if nums[i]:
            for j in range(i * i, n + 1, i):
                nums[j] = False
    return [i for i in range(2, n + 1) if nums[i]]

p = seive(102233)
for _ in range(int(input())):
    n = int(input())
    nums = sorted(map(int, input().split()))
    idx = n - 1
    while p[idx + 1] <= nums[0]:
        idx += 1
    ans = 1e9
    while True:
        cur = sum(abs(p[i + idx - n + 1] - nums[i]) for i in range(n))
        ans = min(ans, cur)
        if p[idx - n + 1] > nums[-1]:
            break
        idx += 1
    print(ans)