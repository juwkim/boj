import sys
input = lambda: sys.stdin.readline().rstrip()

if input()[0] == 'e':
    d = 1
else:
    d = -1
for _ in range(int(input())):
    print(*[chr((ord(c) + d - ord('a')) % 26 + ord('a')) for c in input()], sep='')