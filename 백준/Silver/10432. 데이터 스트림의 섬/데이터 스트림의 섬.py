g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    step, *nums = g()
    ans, stack = 0, []
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
            ans += 1
        if not stack or stack[-1] < num:
            stack.append(num)
    print(step, ans)