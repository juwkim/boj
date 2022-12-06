for i in range(1, 1 + int(input())):
    a, b, c = sorted(map(int, input().split()))
    if c >= b + a:
        state = 'invalid!'
    elif a == b == c:
        state = 'equilateral'
    elif a == b or b == c:
        state = 'isosceles'
    else:
        state = 'scalene'
    print(f'Case #{i}: {state}')