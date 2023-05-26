N = int(input())
stack = []
for sock in input().split():
    if stack and stack[-1] == sock:
        stack.pop()
    else:
        stack.append(sock)
if stack:
    print('impossible')
else:
    print(N << 1)