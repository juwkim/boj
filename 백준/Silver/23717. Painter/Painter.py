import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(1, 1 + int(input())):
    ans = 0
    R, Y, B = 0, 0, 0
    N = int(input())
    for c in input():
        if c == 'R':
            ans += R == 0
            R, Y, B = 1, 0, 0
        elif c == 'Y':
            ans += Y == 0
            R, Y, B = 0, 1, 0
        elif c == 'B':
            ans += B == 0
            R, Y, B = 0, 0, 1
        elif c == 'O':
            ans += (R != 1) + (Y != 1)
            R, Y, B = 1, 1, 0
        elif c == 'P':
            ans += (R != 1) + (B != 1)
            R, Y, B = 1, 0, 1        
        elif c == 'G':
            ans += (Y != 1) + (B != 1)
            R, Y, B = 0, 1, 1
        elif c == 'A':
            ans += (R != 1) + (Y != 1) + (B != 1)
            R, Y, B = 1, 1, 1
        else:
            R, Y, B = 0, 0, 0
    print(f'Case #{_}: {ans}')