stack = []
ans = 'Yes'
for _ in range(int(input())):
    cmd, c = input().split()
    if cmd == 'Add':
        stack.append(c)
    elif not stack or c != stack[-1]:
        ans = 'No'
        break
    else:
        stack.pop()
if stack:
    ans = 'No'
print(ans)