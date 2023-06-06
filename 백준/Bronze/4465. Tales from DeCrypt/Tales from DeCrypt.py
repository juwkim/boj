from math import ceil
def r(a, m):
    global s
    val = s % m / m
    s = (a * s + 1) % m
    return val

a, m, s = map(int, input().split())
while True:
    try:
        line = input()
        for c in line:
            if 0x20 <= ord(c) <= 0x7e:
                c = chr((ord(c) - 32 - ceil(95 - r(a, m) * 95)) % 95 + 32)
            print(c, end='')
        print()
    except Exception as e:
        print(e)
        break