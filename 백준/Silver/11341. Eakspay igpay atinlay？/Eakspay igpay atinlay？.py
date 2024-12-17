import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    for s in input().split():
        i = 0
        while i < len(s) and s[i] not in 'aeiouy':
            i += 1
        if i == 0:
            print(s + 'yay', end=' ')
        else:
            print(s[i:] + s[:i] + 'ay', end=' ')
    print()