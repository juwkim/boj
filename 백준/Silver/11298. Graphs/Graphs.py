g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    A, B = g()
    print(f'y = {A}x + {B}')
    Max = 10 * A + B + 1
    buf = ['*' * Max]
    
    num = A + B - 1
    for i in range(1, 11):
        buf.append(' ' * (Max - num - 2) + '*' + ' ' * num + '*')
        num += A
    for line in zip(*buf):
        print(*line, sep='')