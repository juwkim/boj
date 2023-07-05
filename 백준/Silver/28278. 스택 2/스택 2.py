import sys

input = lambda: sys.stdin.readline().rstrip()

stack = []
for _ in range(int(input())):
    l = input()
    if l[0] == '1':
        stack.append(int(l.split()[1]))
    elif l == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif l == '3':
        print(len(stack))
    elif l == '4':
        print(+(len(stack) == 0))
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)