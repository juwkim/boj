for _ in range(int(input())):
    N, M = map(int, input().split())
    X = int(input().replace(' ', ''))
    Y = int(input().replace(' ', ''))
    table = input().replace(' ', '') * 2
    print(sum(X <= int(table[i:i+M]) <= Y for i in range(N)))