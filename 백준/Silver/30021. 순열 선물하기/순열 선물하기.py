import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
if N == 2:
    print("NO")
elif N == 3:
    print("YES")
    print(1, 3, 2)
else:
    print("YES")
    p = range(2, N + 1, 2)
    print(*reversed(p), end=" ")
    cur = sum(p)
    nums = list(reversed(range(1, N + 1, 2)))
    l = len(nums)
    for _ in range(l):
        for i in range(len(nums)):
            if not is_prime(cur + nums[i]):
                print(nums[i], end=" ")
                cur += nums[i]
                nums.pop(i)
                break