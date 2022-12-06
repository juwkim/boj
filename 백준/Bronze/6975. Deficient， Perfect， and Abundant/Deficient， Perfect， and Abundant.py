for _ in range(int(input())):
    n = int(input())
    t = sum(i for i in range(1, n) if n % i == 0)
    if n == t:
        state = 'a perfect'
    elif n < t:
        state = 'an abundant'
    else:
        state = 'a deficient'
    print(f'{n} is {state} number.\n')