for _ in range(int(input())):
    ans = 'legal'
    stack = []
    for c in input().split()[1]:
        if c == '>':
            if '<' in stack:
                ans = 'illegal'
                break
            stack.append(c)
        elif not stack or stack[-1] != '>':
            ans = 'illegal'
            break
        else:
            stack.pop()
    if stack:
        ans = 'illegal'
    print(ans)