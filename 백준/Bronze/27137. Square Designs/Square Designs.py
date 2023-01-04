M, N = map(int, input().split())
for i in range(max(M, N) + 2):
    if i == 0:
        s = '+' + '-' * (2 * M + 1) + '+' + ' ' * 10 + '+' + '-' * (2 * N + 1) + '+'
        print(s)
        continue
    s = ''
    if i <= M:
        s += 'I' + '-X' * M + '-I'
    elif i == M + 1:
        s += '+' + '-' * (2 * M + 1) + '+'
    else:
        s += ' ' * (2 * M + 3)
    s += ' ' * 10
    if i <= N:
        s += 'I' + '-X' * N + '-I'
    elif i == N + 1:
        s += '+' + '-' * (2 * N + 1) + '+'
    print(s.rstrip())