a, message = input().split()
if a == 'E':
    encode = []
    s, count = message[0], 1
    for alpha in message[1:]:
        if alpha == s:
            count += 1
        else:
            encode += [s, str(count)]
            s, count = alpha, 1
    encode += [s, str(count)]
    print(''.join(encode))
else:
    print(''.join([message[i] * int(message[i+1]) for i in range(0, len(message), 2)]))