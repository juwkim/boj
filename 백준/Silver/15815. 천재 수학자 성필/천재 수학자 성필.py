stack = []
for c in input()[::-1]:
    if c.isdigit() and stack and str(stack[-1]).isdigit():
        a = stack.pop()
        op = stack.pop()
        stack.append(eval(f'{c}{op}{a}'))
    else:
        if c == '/':
            c = '//'
        stack.append(c)
while len(stack) != 1:
    a = stack.pop()
    b = stack.pop()
    op = stack.pop()
    stack.append(eval(f'{a}{op}{b}'))
print(stack.pop())