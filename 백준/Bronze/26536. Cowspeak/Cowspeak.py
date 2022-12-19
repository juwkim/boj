for _ in range(int(input())):
    for s in input().split():
        num = s.count('M') * 16 + s.count('O')
        print(chr(num), end='')
    print()