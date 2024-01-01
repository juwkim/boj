import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
stack = []
nums = g()
for i, num in enumerate(nums):
    while stack and nums[stack[-1]] < num:
        stack.pop()
    print(stack[-1] + 1 if stack else 0, end=" ")
    stack.append(i)