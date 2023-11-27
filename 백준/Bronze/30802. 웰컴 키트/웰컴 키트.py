import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
T, P = g()
cnt = 0
for num in nums:
    cnt += (num + T - 1) // T
print(cnt)
print(*divmod(N, P))