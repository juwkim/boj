from collections import defaultdict

while N:= int(input()):
    
    dic = defaultdict(int)
    diff = defaultdict(int)
    for _ in range(N):
        club1, X, _, Y, club2 = input().split()
        X, Y = int(X), int(Y)
        if X > Y:
            a, b = 3, 0
        elif X == Y:
            a, b = 1, 1
        else:
            a, b = 0, 3
        dic[club1] += a
        dic[club2] += b
        diff[club1] += X - Y
        diff[club2] += Y - X

    for team in sorted(dic, key=lambda x: (-dic[x], -diff[x])):
        print(dic[team], team)
    print()