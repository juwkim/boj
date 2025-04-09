N = int(input())
S, i = input(), 0
while i < N:
    if i + 4 < N and S[i + 4] == '\\':
        print('w', end='')
        i += 9
    else:
        print('v', end='')
        i += 5