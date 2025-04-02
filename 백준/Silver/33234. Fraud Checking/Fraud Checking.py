import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int(input())
    code1 = [input().split() for _ in range(n)]
    code2 = [input().split() for _ in range(n)]
    dic1, dic2 = defaultdict(list), defaultdict(list)
    Map = {}
    idx = 0
    for line1, line2 in zip(code1, code2):
        if len(line1) != len(line2):
            return -1
        for w1, w2 in zip(line1, line2):
            dic1[w1].append(idx)
            dic2[w2].append(idx)
            Map[w1] = w2
            idx += 1
    ans = []
    for k, v in dic1.items():
        if v != dic2[Map[k]]:
            return -1
        if k == Map[k]:
            continue
        ans.append((k, Map[k]))
    return sorted(ans)

ans = solve()
if ans == -1:
    print(-1)
else:
    print(len(ans))
    for l in ans:
        print(*l)