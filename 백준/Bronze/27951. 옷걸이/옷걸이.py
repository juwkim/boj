g = lambda: [*map(int, input().split())]

from collections import Counter

N = int(input())
nums = g()
cnt = Counter(nums)
U, D = g()

if cnt[1] > U or cnt[2] > D:
    print('NO')
else:
    print('YES')
    a = U - cnt[1]
    for c in nums:
        if c == 1:
            print('U', end='')
        elif c == 2:
            print('D', end='')
        elif a:
            print('U', end='')
            a -= 1
        else:
            print('D', end='')