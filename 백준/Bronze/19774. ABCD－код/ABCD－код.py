t = int(input())
for _ in range(t):
    num = input()
    front, back = int(num[:2]), int(num[2:])
    if (front**2 + back**2) % 7 == 1:
        print('YES')
    else:
        print('NO')