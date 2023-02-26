for _ in range(int(input())):
    s = input()
    if len(s) < 3:
        print(-1)
    elif 'O' not in s[1:-1]:
        print(-1)
    elif 'MOO' in s:
        print(len(s) - 3)
    elif 'MOM' in s or 'OOO' in s:
        print(len(s) - 2)
    elif 'OOM' in s:
        print(len(s) - 1)