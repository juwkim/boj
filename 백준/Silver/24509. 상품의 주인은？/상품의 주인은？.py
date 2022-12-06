import sys
input = lambda: sys.stdin.readline().rstrip('\n')

g = lambda: [*map(int, input().split())]

N = int(input())
check = set()

_, *l = zip(*sorted(g() for _ in range(N)))
ans = []
for subject in l:
    Max, idx = -1, 0
    for i in range(N):
        if subject[i] > Max and i not in check:
            Max = subject[i]
            idx = i
    ans.append(idx + 1)
    check.add(idx)
print(*ans)