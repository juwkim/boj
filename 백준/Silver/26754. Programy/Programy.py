import sys
input = sys.stdin.readline
g = lambda: sorted(map(int, input().split()))

N = int(input())
A = g()
M = int(input())
B = g()
ans, i = 0, 0
for num in A:
    while i < M and B[i] < num:
        i += 1
    if i == M:
        break
    ans += 1
    i += 1
print(ans)