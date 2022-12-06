j = 1
while n:=int(input()):
    names = [input() for _ in range(n)]
    print(f'SET {j}')
    for i in range(0, n, 2):
        print(names[i])
    for i in range(n-1-n%2, -1, -2):
        print(names[i])
    j += 1