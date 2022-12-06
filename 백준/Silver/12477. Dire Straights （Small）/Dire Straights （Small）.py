import sys
input = sys.stdin.readline
from collections import defaultdict

for step in range(1, 1 + int(input())):
    dic = defaultdict(list)
    N, *cards = map(int, input().split())
    for card in sorted(cards):
        if dic[card - 1]:
            num = min(dic[card - 1])
            dic[card - 1].remove(num)
            dic[card].append(num + 1)
        else:
            dic[card].append(1)
    if N == 0:
        ans = 0
    else:
        ans = min(min(val) for val in dic.values() if val)
    print(f'Case #{step}: {ans}')