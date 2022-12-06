for _ in range(int(input())):
    q = (int(input()) - 1) % 28
    buf = [['V', '딸기'][int(c)] for c in bin(1 + min(q, 28 - q))[2:].rjust(4, '0')]
    print(*buf, sep='')