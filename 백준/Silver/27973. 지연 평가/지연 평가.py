import sys
input = lambda: sys.stdin.readline().rstrip()

start, stop, step = 1, 1234567890124, 1
for _ in range(int(input())):
    a = input()
    if a == '3':
        print(start)
    else:
        num = int(a[2:])
        match a[0]:
            case '0':
                start += num
                stop += num
            case '1':
                start *= num
                stop *= num
                step *= num
            case '2':
                start += step * num