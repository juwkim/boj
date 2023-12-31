import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict, Counter

N, M = map(int, input().split())
names = set(input().split())
line = defaultdict(list)
for _ in range(M):
    a, b = input().split()
    line[a].append(b)
    line[b].append(a)
cnt = Counter(len(v) for v in line.values())
if sorted(cnt.keys()) not in ([1], [1, 2]) or cnt[1]&1:
    print("EI SAA")
else:
    print("SAAB")
    ones = [k for k, v in line.items() if len(v) == 1]
    ans = []
    for one in ones:
        if one not in names:
            continue
        names.remove(one)
        ans.append(one)
        prev, cur = one, line[one][0]
        while len(line[cur]) == 2:
            ans.append(cur)
            names.remove(cur)
            if line[cur][0] == prev:
                prev, cur = cur, line[cur][1]
            else:
                prev, cur = cur, line[cur][0]
        ans.append(cur)
        names.remove(cur)
    ans.extend(names)
    print(*ans)