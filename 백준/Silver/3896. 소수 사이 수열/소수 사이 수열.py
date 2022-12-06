def Sieve_of_Eratosthenes(N):
    array = [False, False] + [True for i in range(N-1)]
    for i in range(2, int(N**.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    return array

array = Sieve_of_Eratosthenes(1299709)
for i in range(int(input())):
    k = int(input())
    if array[k]:
        print(0)
    else:
        x, y = 1, 1
        while not array[k+x]:
            x += 1
        while not array[k-y]:
            y += 1
        print(x + y)