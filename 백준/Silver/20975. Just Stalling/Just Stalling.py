import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
a = sorted(g(), reverse=True)
b = sorted(g(), reverse=True)
ans, j = 1, 0
for i, num in enumerate(a):
    while j < N and b[j] >= num:
        j += 1
    if i >= j:
        ans = 0
        break
    ans *= j - i
print(ans)