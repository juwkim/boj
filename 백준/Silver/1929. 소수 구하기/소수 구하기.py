def Sieve_of_Eratosthenes(M, N):
    array = [True for i in range(N + 1)]
    for i in range(2, int(N**0.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    return [num for num in range(M, N + 1) if array[num]]

M, N = map(int, input().split())
if M == 1:
    M += 1
for num in Sieve_of_Eratosthenes(M, N):
    print(num)    