i, n = 1, int(input())
while n:
    if n % 2:
        state = 'odd'
    else:
        state = 'even'
    print(f'{i}. {state} {n//2}')
    i += 1
    n = int(input())