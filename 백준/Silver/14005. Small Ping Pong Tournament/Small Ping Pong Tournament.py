n = int(input())
if n == 0:
    print('YES')
elif n == 1:
    print('YES' if int(input()) >= int(input()) else 'NO')
elif n == 2:
    dudu = int(input())
    a = min(int(input()) for _ in range(3))
    print('YES' if dudu - a >= 0 else 'NO')
else:
    dudu = int(input())
    a = min(int(input()) for _ in range(7))
    print('YES' if dudu - a >= 0 else 'NO')