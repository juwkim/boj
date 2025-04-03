g = lambda: [*map(int, input().split())]

N = int(input())
A, B = g(), g()
if A[0] == 0 or B[-1] == 0:
    print(0)
elif all(A) and all(B):
    print(2)
else:
    ans = 1
    for i in range(N - 1):
        if A[i] == 0 and B[i + 1] == 0:
            ans = 0
            break
        if A[i + 1] == 0 and B[i] == 0:
            ans = 0
            break
    print(ans)