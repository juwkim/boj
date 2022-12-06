g = lambda: [*map(int, input().split())]

alpha = 'abcdefghijklmnopqrstuvwxyz'
A, B = g()
for i in range(B):

    word = []
    num = i
    while True:
        num, q = divmod(num, 26)
        word.append(alpha[q])
        if num == 0:
            break
    print(''.join(word), end=' ')