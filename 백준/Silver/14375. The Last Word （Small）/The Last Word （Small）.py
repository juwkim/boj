from collections import deque
for i in range(1, 1 + int(input())):
    c, *l = input()
    dq = deque([c])
    for c in l:
        if c < dq[0]:
            dq.append(c)
        else:
            dq.appendleft(c)
    print(f'Case #{i}:', ''.join(dq))