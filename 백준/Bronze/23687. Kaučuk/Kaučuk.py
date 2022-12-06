a, b, c = 0, 0, 0
for _ in range(int(input())):
    t, name = input().split()
    if t == 'section':
        a, b, c = a + 1, 0, 0
        print(a, name)
    elif t == 'subsection':
        b, c = b + 1, 0
        print(f'{a}.{b}', name)
    else:
        c += 1
        print(f'{a}.{b}.{c}', name)