import sys
input = sys.stdin.readline

one, two = [], []
order = []
for i in range(int(input())):
    cmd, *arg = input().split()
    match cmd:
        case '1':
            one.append(arg[0])
            order.append(1)
        case '2':
            two.append(arg[0])
            order.append(2)
        case '3':
            if order:
                num = order.pop()
                if num == 1:
                    one.pop()
                else:
                    two.pop()
if one or two:
    print(*two[::-1], *one, sep='')
else:
    print(0)