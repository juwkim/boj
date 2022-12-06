for i in range(1, 1 + int(input())):
    students, brownies = map(int, input().split())
    print(f'Practice #{i}: {students} {brownies}')
    for _ in range(int(input())):
        n = int(input())
        while brownies <= n:
            brownies <<= 1
        brownies -= n
        print(n, brownies)
    print()