g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = []
stack = []
for num in reversed(nums):
    while stack and stack[-1] <= num:
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(num)
print(*ans[::-1])