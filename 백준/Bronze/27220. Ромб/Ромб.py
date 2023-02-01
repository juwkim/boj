n = int(input())
a = int(input())
b = int(input())

k = n >> 1
for i in range(n):
    for j in range(n):
        if a <= abs(i - k) + abs(j - k) <= b:
            print('*', end='')
        else:
            print('.', end='')
    print()