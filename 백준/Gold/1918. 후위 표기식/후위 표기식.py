stack = []
for c in input():
    if c.isalpha():
        print(c, end='')
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    elif c in '+-':
        while stack and stack[-1] in '+-*/':
            print(stack.pop(), end='')
        stack.append(c)
    else:
        while stack and stack[-1] in '*/':
            print(stack.pop(), end='')
        stack.append(c)
while stack:
    print(stack.pop(), end='')