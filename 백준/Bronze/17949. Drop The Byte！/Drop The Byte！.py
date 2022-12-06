pwd = input()
N = int(input())
form = input().split()

i = 0
while i < len(pwd):
    a = form.pop(0)[0]
    if a == 'i':
        print(int(pwd[i:i+8], 16), end=' ')
        i += 8
    elif a == 'c':
        print(int(pwd[i:i+2], 16), end=' ')
        i += 2
    else:
        print(int(pwd[i:i+16], 16), end=' ')
        i += 16