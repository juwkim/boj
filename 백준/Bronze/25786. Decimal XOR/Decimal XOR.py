a, b = input(), input()
if len(a) < len(b):
    a = '0' * (len(b) - len(a)) + a
else:
    b = '0' * (len(a) - len(b)) + b

for p, q in zip(a, b):
    if p <= '2' and q <= '2':
        print('0', end='')
    elif p >= '7' and q >= '7':
        print('0', end='')
    else:
        print('9', end='')