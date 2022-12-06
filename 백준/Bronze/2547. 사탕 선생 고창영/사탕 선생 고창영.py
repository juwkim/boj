for _ in range(int(input())):
    input()
    n = int(input())
    print('NO' if sum(int(input()) for _ in range(n)) % n else 'YES')