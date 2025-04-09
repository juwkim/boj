import sys
input = sys.stdin.readline

A = []
px = [0]
for _ in range(int(input())):
    cmd, *x = map(int, input().split())
    match cmd:
        case 1:
            x = x[0]
            A.append(x)
            px.append(px[-1] + x)
        case 2:
            l = len(A)
            idx = l >> 1
            a, b = px[idx] - px[0], px[l] - px[idx]
            if b < a:
                print(b)
                A = A[:idx]
                px = px[:idx+1]
            else:
                print(a)
                A = A[idx:]
                px = px[idx:]
print(*A)