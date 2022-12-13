dic = {')': '(', '}': '{', ']': '['}
while (s:= input()) != '#':
    stack = []
    ans = 'Legal'
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in dic and (not stack or stack.pop() != dic[c]):
            ans = 'Illegal'
            break
    if stack:
        ans = 'Illegal'
    print(ans)