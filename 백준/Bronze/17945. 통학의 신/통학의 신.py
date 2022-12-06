A, B = map(int, input().split())
if A**2 == B:
    print(-A)
else:
    print(int(-A-(A**2-B)**.5), int(-A+(A**2-B)**.5))