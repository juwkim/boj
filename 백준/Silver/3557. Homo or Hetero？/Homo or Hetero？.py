import sys
input = sys.stdin.readline
from collections import Counter

cnt = Counter()
value_set, multi_set = set(), set()
for _ in range(int(input())):
    op, num = input().split()
    num = int(num)
    if op[0] == 'i':
        cnt[num] += 1
        value_set.add(num)
        if cnt[num] == 2:
            multi_set.add(num)
    elif cnt[num]:
        cnt[num] -= 1
        if cnt[num] == 1:
            multi_set.remove(num)
        elif cnt[num] == 0:
            value_set.remove(num)
    if multi_set:
        if len(value_set) > 1:
            ans = "both"
        else:
            ans = "homo"
    elif len(value_set) > 1:
        ans = "hetero"
    else:
        ans = "neither"
    print(ans)