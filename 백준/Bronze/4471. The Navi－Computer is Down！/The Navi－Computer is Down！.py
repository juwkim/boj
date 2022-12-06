for _ in range(int(input())):
    src = input()
    a = map(float, input().split())
    dest = input()
    b = map(float, input().split())
    dist = sum((x - y)**2 for x, y in zip(a, b))**.5
    print(f'{src} to {dest}: {dist:#.2f}')