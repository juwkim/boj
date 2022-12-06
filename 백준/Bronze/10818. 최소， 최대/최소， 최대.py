import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
print(min(nums), max(nums))