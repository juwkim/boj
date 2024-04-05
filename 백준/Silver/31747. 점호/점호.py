from collections import deque

N, K, *A = map(int, open(0).read().split())
one, two = deque(), deque()
for i, num in enumerate(A):
    if num == 1:
        one.append(i)
    else:
        two.append(i)
t = 0
while one or two:
    t += 1
    if one and two:
        if abs(one[0] - two[0]) < K:
            one.popleft()
            two.popleft()
        elif one[0] < two[0]:
            one.popleft()
        else:
            two.popleft()
    elif one:
        one.popleft()
    else:
        two.popleft()
print(t)