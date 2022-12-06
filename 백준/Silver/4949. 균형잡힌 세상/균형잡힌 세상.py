from collections import deque
while (s:=input()) != '.':
    deq = deque()
    flag = 'yes'
    for t in s:
        if t in '([':
            deq.append(t)
        elif t == ')':
            if not deq or deq.pop() != '(':
                flag = 'no'
                break
        elif t == ']':
            if not deq or deq.pop() != '[':
                flag = 'no'
                break
    print('no' if deq else flag)