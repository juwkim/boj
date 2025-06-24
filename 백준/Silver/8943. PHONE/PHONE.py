import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import pairwise

for _ in range(int(input())):
    n = bytearray(26)
    p = [tuple(sorted(x)) for x in pairwise(map(int, input()))]
    for l in p:
        match l:
            case (1, 2) | (1, 3) | (2, 3):
                n[0] = 1
            case (4, 5) | (4, 6) | (5, 6):
                n[1] = 1
            case (7, 8) | (7, 9) | (8, 9):
                n[2] = 1
            case (1, 4) | (1, 7) | (4, 7):
                n[3] = 1
            case (0, 2) | (2, 5) | (2, 8) | (0, 5) | (5, 8) | (0, 8):
                n[4] = 1
            case (3, 6) | (3, 9) | (6, 9):
                n[5] = 1
            case (2, 6):
                n[6] = 1
            case (1, 5) | (1, 9) | (5, 9):
                n[7] = 1
            case (4, 8):
                n[8] = 1
            case (0, 7):
                n[9] = 1
            case (2, 4):
                n[10] = 1
            case (3, 5) | (3, 7) | (5, 7):
                n[11] = 1
            case (6, 8):
                n[12] = 1
            case (0, 9):
                n[13] = 1
            case (1, 8):
                n[14] = 1
            case (0, 4):
                n[15] = 1
            case (2, 9):
                n[16] = 1
            case (2, 7):
                n[17] = 1
            case (3, 8):
                n[18] = 1
            case (0, 6):
                n[19] = 1
            case (1, 6):
                n[20] = 1
            case (4, 9):
                n[21] = 1
            case (3, 4):
                n[22] = 1
            case (6, 7):
                n[23] = 1
            case (0, 1):
                n[24] = 1
            case (0, 3):
                n[25] = 1
    cnt = sum(n)
    if (2, 5) in p and (0, 8) in p and all(t not in p for t in ((2, 8), (0, 2), (5, 8), (0, 5))):
        cnt += 1
    if cnt <= 3:
        print('EXCELLENT')
    elif cnt == 4:
        print('GOOD')
    else:
        print('BAD')