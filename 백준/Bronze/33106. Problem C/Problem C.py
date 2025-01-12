import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    l = len(S := input())
    i = 0
    while i < l:
        if S[i] != 'c':
            c = S[i]
            i += 1
        elif i + 1 < l and S[i + 1] == 'h':
            c = 'c'
            i += 2
        elif i + 1 < l and S[i + 1] in "eiy":
            c = 's'
            i += 1
        else:
            c = 'k'
            i += 1
        print(c, end='')
    print()