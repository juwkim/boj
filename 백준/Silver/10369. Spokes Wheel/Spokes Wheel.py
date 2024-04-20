from collections import deque
from copy import deepcopy

for tc in range(1, 1 + int(input())):
    N1, N2 = map(lambda x: int(x, 16), input().split())
    N1 = deque([(N1 >> i) & 1 for i in range(32)])
    N2 = deque([(N2 >> i) & 1 for i in range(32)])
    ans = "Not possible"
    l, r = deepcopy(N1), deepcopy(N1)
    for cnt in range(17):
        if l == N2 and r == N2:
            ans = f"{cnt} Any"
            break
        elif l == N2:
            ans = f"{cnt} Left"
            break
        elif r == N2:
            ans = f"{cnt} Right"
            break
        l.rotate(1)
        r.rotate(-1)
    print(f"Case #{tc}: {ans}")