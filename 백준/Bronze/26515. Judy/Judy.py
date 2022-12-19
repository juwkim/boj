g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    a, *l = g()
    for num in l:
        if 97 <= num <= 122 or 65 <= num <= 90:
            c = chr(num).lower()
        else:
            c = '-'
        print(c, end='')
    if 97 <= a <= 122 or 65 <= a <= 90:
        c = chr(a).lower()
    else:
        c = '-'
    print(c, end='')
    print('ay')