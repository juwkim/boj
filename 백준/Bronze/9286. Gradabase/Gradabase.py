for i in range(1, int(input())+1):
    print(f'Case {i}:')
    for _ in range(int(input())):
        n = int(input())
        if n < 6:
            print(n+1)