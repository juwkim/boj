H = int(input())
buf = ['*' * i + ' ' * (H - i << 1) + '*' * i for i in range(1, H, 2)]
buf += ['*' * (2 * H)] + buf[::-1]
for line in buf:
    print(line)