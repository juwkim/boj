def g(): return [*map(int, input().split())]

n = int(input())
stack = []
for num in g():
    if stack and (stack[-1] + num) & 1 == 0:
        stack.pop()
    else:
        stack.append(num)
print(len(stack))