from math import log
for i in range(1, 1+int(input())):
    n, middle = int(input()), 0
    t = 2 **(int(log(n, 2)))
    while True:
        if n == t:
            print(f'Case #{i}: {middle}')
            break
        else:
            middle, t, n = int(n > t), t//2, n%t