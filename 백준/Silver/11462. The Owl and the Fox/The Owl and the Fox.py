import sys
input = lambda: sys.stdin.readline().rstrip()
while (N := input()) != 'END':
    N = [*N]
    idx = -1
    while N[idx] == '0':
        idx -= 1
    N[idx] = chr(ord(N[idx]) - 1)
    print(int(''.join(N)))