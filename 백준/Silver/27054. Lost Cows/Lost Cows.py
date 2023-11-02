import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
buf = [*range(1, N + 1)]
ans = []
for num in reversed([int(input()) for _ in range(N - 1)]):
    ans.append(buf.pop(num))
ans.append(buf.pop())
print(*ans[::-1])