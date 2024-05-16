import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = set()
ans = []
for _ in range(N):
    *l, name = input().split()
    Max, day = 0, 0
    for a in l:
        if a == '.':
            day += 1
        else:
            Max = max(Max, day)
            day = 0
    Max = max(Max, day)
    ans.append((Max, name))
    cnt.add(Max)
print(len(cnt))
for a, b in ans:
    print(a, b)