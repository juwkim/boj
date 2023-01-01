input = __import__('sys').stdin.readline

from collections import defaultdict
def g(): return tuple(map(int, input().split()))


def solve(a, b):
    global dp
    if (a, b) in dp:
        return dp[(a, b)]
    
    r = 0
    for i in range(Q):
        if a <= nums[i] <= b:
            tmp = (b - a) + solve(a, nums[i] - 1) + solve(nums[i] + 1, b)
            if r == 0 or tmp < r:
                r = tmp
        if nums[i] > b:
            break
    
    dp[(a, b)] = r
    return r

for step in range(1, 1 + int(input())):
    P, Q = g()
    nums = g()
    dp = defaultdict(int)
    ans = solve(1, P)
    print(f'Case #{step}: {ans}')