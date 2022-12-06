ans = 0
for _ in range(int(input())):
    stack = []
    for c in input():
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    ans += not stack
print(ans)