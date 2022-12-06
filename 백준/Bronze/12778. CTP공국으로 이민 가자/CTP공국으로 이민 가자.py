for _ in range(int(input())):
    if input()[-1] == 'C':
        print(*[ord(i) - 64 for i in input().split()])
    else:
        print(*[chr(int(i) + 64) for i in input().split()])      