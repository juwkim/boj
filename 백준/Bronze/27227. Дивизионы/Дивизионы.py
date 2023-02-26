N = int(input())

s = input()
if N <= 1600:
    if '3' in s:
        print(3)
    else:
        for c in s:
            print(c)
elif N <= 1900:
    if '2' in s:
        print(2)
    else:
        for c in s:
            if c == '1':
                print('1')
            else:
                print(c + '*')
else:
    if '1' in s:
        print(1)
    else:
        for c in s:
            print(c + '*')