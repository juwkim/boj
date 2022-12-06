import sys
input = lambda: sys.stdin.readline().rstrip('\n')

N = int(input())
nums = [float(input()) for _ in range(N)]
nums.sort()
for num in nums[:7]:
    print("%.3f" % num)