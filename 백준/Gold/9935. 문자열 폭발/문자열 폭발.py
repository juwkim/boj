s, p = input(), [*input()]
stack = []
for c in s:
    stack.append(c)
    if stack[-len(p):] == p:
        for _ in range(len(p)):
            stack.pop()
if stack:
    print(*stack, sep='')
else:
    print('FRULA')