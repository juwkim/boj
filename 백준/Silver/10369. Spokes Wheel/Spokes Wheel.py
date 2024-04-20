from collections import deque

for tc in range(1, 1 + int(input())):
    N1, N2 = map(lambda x: int(x, 16), input().split())
    ans = "Not possible"
    l, r = N1, N1
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
        l = ((l & ((1 << 31) - 1)) << 1) | (l >> 31)
        r = (r >> 1) | ((r & 1) << 31)
    print(f"Case #{tc}: {ans}")