ans = 0
s = input()
stack = [] 

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i-1] == '(':
        stack.pop()
        ans += len(stack)
    else:
        stack.pop()
        ans += 1
print(ans)