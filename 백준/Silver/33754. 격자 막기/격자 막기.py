g = lambda: [*map(int, input().split())]

N = int(input())
A, B = g(), g()
if A[0] == 0 or B[-1] == 0:
    assert False
elif all(A) and all(B):
    print(2)
else:
    ans = 1
    for i in range(N - 1):
        if (0, 0) in ((A[i], B[i + 1]), (A[i + 1], B[i]), (A[i], B[i])):
            ans = 0
            break
    print(ans)