from statistics import median
while (name:=input()) != '#':
    M, S = map(int, input().split())
    for _ in range(int(input())):
        a, b = input().split()
        S = median([0, S + int(b) * (-1)**(a == 'S'), 100])
    print(name, S)