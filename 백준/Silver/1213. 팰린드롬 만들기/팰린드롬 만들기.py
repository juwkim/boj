from collections import deque
buf = [0] * 26
for c in input():
    buf[ord(c) - 65] += 1

odd = [i for i in range(26) if buf[i] & 1]
if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    dq = deque()
    if len(odd):
        dq.append(chr(odd[0] + 65))
        buf[odd[0]] -= 1
    
    for i in range(25, -1, -1):
        a = buf[i] // 2
        c = chr(i + 65)
        dq.appendleft(c * a)
        dq.append(c * a)
    
    print(*dq, sep='')