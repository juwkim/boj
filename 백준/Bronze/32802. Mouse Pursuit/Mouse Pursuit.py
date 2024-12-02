import sys
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    cmd, *nums = input().split()
    s, c, g = map(int, nums)
    l.append((cmd, s, c, g))
k = int(input())
C, G = 0, 0
for cmd, s, c, g in l:
    if s > k:
        continue
    if cmd[0] == 'C':
        C += c
        G += g
    else:
        C -= c
        G -= g
print(C, G)