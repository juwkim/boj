import sys
input = sys.stdin.readline

A, px = [], [0]
for _ in range(int(input())):
    cmd, *x = map(int, input().split())
    match cmd:
        case 1:
            A.append(x[0])
            px.append(px[-1] + x[0])
        case 2:
            i = len(A) >> 1
            a, b = px[i] - px[0], px[-1] - px[i]
            if b < a:
                print(b)
                A, px = A[:i], px[:i+1]
            else:
                print(a)
                A, px = A[i:], px[i:]
print(*A)