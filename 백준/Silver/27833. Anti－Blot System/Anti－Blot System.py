for _ in range(int(input())):
    input()
    a, _, b, _, c = input().split()
    if 'm' in a:
        a = int(c) - int(b)
    elif 'm' in b:
        b = int(c) - int(a)
    else:
        c = int(a) + int(b)
    print(f'{a} + {b} = {c}')