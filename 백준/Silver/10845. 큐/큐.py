que, I = [], open(0).readline
for _ in range(int(I())):
    Q = I().split()
    s = Q[0]
    if s == 'push':
        que.append(Q[1])
    elif s == 'pop':
        print(que.pop(0) if que else -1)
    elif s == 'size':
        print(len(que))
    elif s == 'empty':
        print(int(que == []))
    elif s == 'front':
        print(que[0] if que else -1)
    else:
        print(que[-1] if que else -1)