import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    nums = []
    for i in range(1, int(m**0.5) + 1):
        if m % i == 0:
            nums.append(i)
            if i > 1 and i != m // i:
                nums.append(m // i)
    def solve(i, cur):
        if i == len(nums):
            return False
        num = cur + nums[i]
        if num == m:
            return True
        if num < m:
            ret = solve(i + 1, num)
            if ret:
                return True
        return solve(i + 1, cur)
    if solve(0, 0):
        print("Semiperfect")
    else:
        print("NOT Semiperfect")