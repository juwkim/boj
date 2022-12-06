A, B = input(), input()
C = input()
if all(C in s for s in [A, B]):
    print('YES')
else:
    print('NO')