from collections import deque
n = int(input())
nums = [int(input()) for _ in range(n)]

deq, i, s, a = deque(), 1, 0, ''
while s < n:
    if not deq or deq[-1] < nums[s]:
        deq.append(i)
        i += 1
        a += '+'
    else:
        if deq.pop() > nums[s]:
            break
        s += 1
        a += '-'
if len(a) == 2*n:
    print(*a)
else:
    print('NO')