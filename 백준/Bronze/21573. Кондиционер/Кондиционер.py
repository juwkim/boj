room, cond = map(int, input().split())
mode = input()
if mode == 'fan':
    print(room)
elif mode == 'auto':
    print(cond)
elif mode == 'freeze':
    print(min(room, cond))
else:
    print(max(room, cond))