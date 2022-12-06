for _ in range(1, 1 + int(input())):
    C, *data = input().split()
    C = int(C)
    dic = {}
    for i in range(C):
        a, b, c = data[i]
        dic[a+b] = c
        dic[b+a] = c
    D = int(data[C])
    opposed = data[C+1:C+1+D]
    N = int(data[-2])
    msg = data[-1]
    
    stack = [msg[0]]
    for i in range(1, N):
        if stack:
            a, b = stack.pop(), msg[i]
    
            if a + b in dic:
                stack.append(dic[a+b])
            elif b + a in dic:
                stack.append(dic[b+a])
            else:
                stack.extend([a, b])
            
            for s in opposed:
                if s[0] in stack and s[1] in stack:
                    stack = []
                    break
        else:
            stack.append(msg[i])
    print(f'Case #{_}: [{", ".join(stack)}]')