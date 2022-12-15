buf = [input().split() for _ in range(int(input()))]
cur, register, stack = 0, None, []
while True:
    cmd, *l = buf[cur]
    if cmd == 'PUSH':
        stack.append(int(l[0]))
    elif cmd == 'STORE':
        register = stack.pop()
    elif cmd == 'LOAD':
        stack.append(register)
    elif cmd == 'PLUS':
        num = stack.pop()
        stack[-1] += num
    elif cmd == 'TIMES':
        num = stack.pop()
        stack[-1] *= num
    elif cmd == 'IFZERO':
        num = stack.pop()
        if num == 0:
            cur = int(l[0]) - 1
    else:
        break
    cur += 1
print(stack[-1])