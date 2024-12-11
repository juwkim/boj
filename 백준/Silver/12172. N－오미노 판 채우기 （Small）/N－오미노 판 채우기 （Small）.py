import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    X, *l = map(int, input().split())
    R, C = sorted(l)
    ans = "GABRIEL"
    match X:
        case 2:
            if R * C & 1:
                ans = "RICHARD"
        case 3:
            if R * C % 3 or R == 1:
                ans = "RICHARD"
        case 4:
            if R < 3 or C != 4:
                ans = "RICHARD"
    print(f"Case #{tc}: {ans}")