from math import trunc

N = int(input())
S = input()
A, i, printed = 0, 0, False
while i < len(S) and S[i].isnumeric():
    A = A * 10 + int(S[i])
    i += 1
for _ in range(N):
    cmd = S[i]
    i += 1
    if cmd == 'C':
        print(A, end=' ')
        printed = True
    else:
        B = 0
        if i == len(S):
            break
        while i < len(S) and S[i].isnumeric():
            B = B * 10 + int(S[i])
            i += 1
        match cmd:
            case 'S':
                A -= B
            case 'M':
                A *= B
            case 'U':
                A = trunc(A / B)
            case 'P':
                A += B
if not printed:
    print("NO OUTPUT")