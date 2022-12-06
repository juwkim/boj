g = lambda: [*map(int, input().split())]

from collections import defaultdict
for _ in range(1, 1 + int(input())):
    dic = defaultdict(int)
    Map = [g() for _ in range(3)]
    ans = 0
    ans += (Map[0][1] * 2 == Map[0][0] + Map[0][2])
    ans += (Map[2][1] * 2 == Map[2][0] + Map[2][2])
    ans += (Map[1][0] * 2 == Map[0][0] + Map[2][0])
    ans += (Map[1][1] * 2 == Map[0][2] + Map[2][2])
    
    dic[Map[0][0] + Map[2][2]] += 1
    dic[Map[2][0] + Map[0][2]] += 1
    dic[Map[0][1] + Map[2][1]] += 1
    dic[Map[1][0] + Map[1][1]] += 1

    l = [v for k, v in dic.items() if k%2 == 0]
    if l:
        ans += max(l)
    print(f'Case #{_}: {ans}')