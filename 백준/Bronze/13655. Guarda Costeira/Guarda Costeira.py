import sys
while True:
    n = sys.stdin.readline()
    if n:
        D, VF, VG = map(int, n.split())
        print('S' if (D**2 + 144)**.5 / VG <= 12 / VF else 'N')
    else:
        break