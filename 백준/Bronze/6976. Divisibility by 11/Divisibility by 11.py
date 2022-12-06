for _ in range(int(input())):
    s = int(input())
    print(n:= s)
    while n > 99:
        r, q = divmod(n, 10)
        print(n:= r - q)
    print(f'The number {s} is' + ' not' * (n % 11 != 0) + ' divisible by 11.\n')