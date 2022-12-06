g = lambda: [*map(int, input().split())]

N, M, X = g()
nums = g()

buf = []
for i in range(M):
    h = nums[i]
    if h < X:
        if i % 3 == 2:
            line = '.' * (N - X) + '-' + '|' * (X - 1 - h) + '#' * h
        else:
            line = '.' * (N - X) + '-' + '.' * (X - 1 - h) + '#' * h
    else:
        line = '.' * (N - h) + '#' * (h - X) + '*' + '#' * (X - 1)
    buf.append(line)
for line in zip(*buf):
    print(*line, sep='')