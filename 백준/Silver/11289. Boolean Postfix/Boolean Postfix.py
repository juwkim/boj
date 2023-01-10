cmd = {'A': '&', 'R': '|', 'X': '^'}
for _ in range(int(input())):
    N, *buf = input().split()
    stack = []
    for c in buf:
        if c in '01':
            stack.append(int(c))
        elif c == 'N':
            stack.append(1 - stack.pop())
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(eval(f'{a}{cmd[c]}{b}'))
    print(stack.pop()) 