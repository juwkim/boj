for _ in range(int(input())):
    s = input()
    for a, b in zip(' ' + s, s):
        if a != b:
            print(b, end='')
    print()