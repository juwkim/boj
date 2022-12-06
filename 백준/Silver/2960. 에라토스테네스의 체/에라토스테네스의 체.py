def Sieve_of_Eratosthenes(N, K):
    array = [True for i in range(N+1)]
    for i in range(2, N+1):
        if array[i]:
            K -= 1
            if K == 0:
                return i
            j = 2
            while i * j <= N:
                K -= array[i * j]
                if K == 0:
                    return i * j
                array[i * j] = False
                j += 1

N, K = map(int, input().split())
num = Sieve_of_Eratosthenes(N, K)
print(num)