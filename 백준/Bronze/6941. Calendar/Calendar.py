cur, num = map(int, input().split())
print('Sun Mon Tue Wed Thr Fri Sat')
print(' ' * (4 * (cur - 1)), end='')
for i in range(cur, num + cur):
    print("% 3d" % (i - cur + 1), end=' ')
    if i % 7 == 0:
        print()