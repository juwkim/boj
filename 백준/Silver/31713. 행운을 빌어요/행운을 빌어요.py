import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    if A * 4 < B:
        cnt = B - A * 4
        ans = cnt // 4
        match cnt % 4:
            case 0:
                pass
            case 1:
                ans += 1 + max(0, 2 - ans - A)
            case 2:
                ans += 1 + max(0, 1 - ans - A)
            case 3:
                ans += 1
    elif B < A * 3:
        ans = A * 3 - B
    else:
        ans = 0
    print(ans)