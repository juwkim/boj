import sys
input = sys.stdin.readline

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
k = [[(0, 0)] for _ in range(10000)]
for Y, X1, X2 in nums:
    k[X1].append((Y, 1))
    k[X2 - 1].append((Y, 1))
    for i in range(X1 + 1, X2 - 1):
        k[i].append((Y, 0))
for i in range(1, 10000):
    k[i].sort()
ans = 0
for i in range(1, 10000):
    l = k[i]
    for i in range(1, len(l)):
        if l[i][1]:
            ans += l[i][0] - l[i - 1][0]
print(ans)