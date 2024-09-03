import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
A = {num: i for i, num in enumerate(g())}
ans, jump = [], -1
for i, num in enumerate(g(), 0):
    if A[num] - i > jump:
        jump = A[num] - i
        ans = [num]
    elif A[num] - i == jump:
        ans.append(num)
print(*ans)