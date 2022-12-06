import sys
stack = []
for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop() if len(stack) else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(0 if len(stack) else 1)
    else:
        print(stack[-1] if len(stack) else -1)