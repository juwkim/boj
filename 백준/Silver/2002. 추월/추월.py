import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]
idx = N - 1
ans = 0
check = set()
for i in range(N - 1, -1, -1):
    if A[i] == B[idx]:
        idx -= 1
        while idx >= 0 and B[idx] in check:
            idx -= 1
    else:
        check.add(A[i])
        ans += 1
print(ans)