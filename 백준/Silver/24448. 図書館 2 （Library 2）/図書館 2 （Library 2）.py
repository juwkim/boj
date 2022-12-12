import sys
input = lambda: sys.stdin.readline().rstrip()
stack = []
for _ in range(int(input())):
    s = input()
    if s == 'READ':
        print(stack.pop())
    else:
        stack.append(s)