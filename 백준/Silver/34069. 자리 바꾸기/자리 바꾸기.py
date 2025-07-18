import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
if N & 1 and M & 1:
    print("No")
elif N & 1:
    print("Yes")
    for _ in range(N):
        line = g()
        print(*[line[i^1] for i in range(M)])
else:
    print("Yes")
    nums = [g() for _ in range(N)]
    for i in range(N):
        for j in range(M):
            print(nums[i^1][j], end=' ')
        print()