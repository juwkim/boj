import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    a, b = 0, 0
    while s[a] == '!':
        a += 1
    while s[-1-b] == '!':
        b += 1
    n = int(s[a])
    if b:
        n = 1
    if a & 1:
        n ^= 1
    print(n)