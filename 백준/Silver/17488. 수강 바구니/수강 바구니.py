import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]

N, M = g()
L = g()
buf = [[] for _ in range(M)]
for i in range(N):
    nums = g()
    for j in range(len(nums) - 1):
        buf[nums[j]-1].append(i)

ans = [set() for _ in range(N)]
for i in range(M):
    if len(buf[i]) <= L[i]:
        for student in buf[i]:
            ans[student].add(i+1)

for i in range(N):
    nums = g()
    for j in range(len(nums) - 1):
        buf[nums[j]-1].append(i)

for i in range(M):
    if len(buf[i]) <= L[i]:
        for student in buf[i]:
            ans[student].add(i+1)

for student in ans:
    if student:
        print(*sorted(student))
    else:
        print('망했어요')