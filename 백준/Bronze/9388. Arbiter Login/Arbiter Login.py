for i in range(int(input())):
    a, b = input().split()
    c = ''.join([i for i in a if i > '9'])
    if a == b:
        v = 'Login successful.'
    elif len(a) < len(b):
        v = 'Wrong password.'
    elif (len(a) > len(c) and c.swapcase() == b):
        v = 'Wrong password. Please, check your caps lock and num lock keys.'
    elif a == b.swapcase():
        v = 'Wrong password. Please, check your caps lock key.'
    elif (len(a) > len(c) and c == b):
        v = 'Wrong password. Please, check your num lock key.'
    else:
        v = 'Wrong password.'
    print(f'Case {i+1}:', v)