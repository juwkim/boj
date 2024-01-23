import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

K, L, N = g()
zero, one = 0, 0
used = False
ans = []
for i, c in enumerate(input() + '0' * L):
    if c == '0':
        one = 0
        zero += 1
        if used and zero == L:
            used = False
            ans.append(i + 1)
    else:
        zero = 0
        one += 1
        if one == K:
            used = True
if ans:
    print(*ans)
else:
    print("NIKAD")