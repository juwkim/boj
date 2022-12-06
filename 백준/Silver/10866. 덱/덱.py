from collections import deque
deq, I = deque(), open(0).readline
for _ in range(int(I())):
    Q = I().split()
    s = Q[0]
    if s == 'push_front':
        deq.appendleft(Q[1])
    elif s == 'push_back':
        deq.append(Q[1])
    elif s == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif s == 'pop_back':
        print(deq.pop() if deq else -1)    
    elif s == 'size':
        print(len(deq))
    elif s == 'empty':
        print(int(len(deq) == 0))
    elif s == 'front':
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)