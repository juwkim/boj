for i in range(1, 1+int(input())):
    a, b = map(int, input().split())
    if a//b and a%b:
        print(f'Case {i}: {a//b} {a%b}/{b}')
    elif a//b:
        print(f'Case {i}: {a//b}')
    elif a%b:
        print(f'Case {i}: {a%b}/{b}')
    else:
        print(f'Case {i}: 0')