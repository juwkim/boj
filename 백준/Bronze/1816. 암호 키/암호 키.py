for _ in range(int(input())):
    S = int(input())
    if all(S % i for i in range(2, 1000001)):
        print('YES')
    else:
        print('NO')