for _ in range(int(input())):
    a, b = map(float, input().split())
    ans = 2 * a / b
    print(f'The height of the triangle is {ans:#.2f} units')