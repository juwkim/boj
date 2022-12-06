g = lambda: [*map(int, input().split())]

from itertools import cycle
while sum(s:= g()):
    n, p = s
    num = p
    cnt = [0] * n
    
    for idx in cycle(range(n)):
        if p:
            p -= 1
            cnt[idx] += 1
            if p == 0 and cnt[idx] == num:
                print(idx)
                break
        else:
            p += cnt[idx]
            cnt[idx] = 0