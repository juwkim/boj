stack = []
s = input()
res, tmp = 0, 1
for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])
    elif s[i] == ')':
        if not stack or stack.pop() != '(':
            res = 0
            break
        if s[i-1] == '(':
            res += tmp
        tmp //= 2
    else:
        if not stack or stack.pop() != '[':
            res = 0
            break
        if s[i-1] == '[':
            res += tmp
        tmp //= 3
if stack:
    res = 0
print(res)