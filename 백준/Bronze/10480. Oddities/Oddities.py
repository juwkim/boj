for _ in range(int(input())):
    x = int(input())
    print(f'{x} is', ['even', 'odd'][x % 2])