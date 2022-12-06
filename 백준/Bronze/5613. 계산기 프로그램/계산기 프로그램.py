import sys

inputs = sys.stdin.read().split()
nums = [int(inputs[2 * i]) for i in range(len(inputs) // 2)]
operators = [inputs[2 * i + 1] for i in range(len(inputs) // 2)]

ans = nums[0]
for i in range(1, len(operators)):
    if operators[i - 1] == '+':
        ans += nums[i]
    elif operators[i - 1] == '-':
        ans -= nums[i]
    elif operators[i - 1] == '*':
        ans *= nums[i]
    else:
        ans //= nums[i]
print(ans)