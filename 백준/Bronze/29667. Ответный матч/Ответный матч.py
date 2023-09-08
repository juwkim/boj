a1, b2 = map(int, input().split(':'))
b1, a2 = map(int, input().split(':'))

if b1 <= a1 and a2 <= b2:
    print("YES")
else:
    print("NO")