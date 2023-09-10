import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

J, N = g()
ans = 0
for _ in range(N):
    num = 0
    for c in input():
        if c.isupper():
            num += 4
        elif c == ' ':
            num += 1
        else:
            num += 2
    ans += num <= J
print(ans)