import sys

def Sieve_of_Eratosthenes(M, N):
    array = [True for i in range(N + 1)]
    for i in range(2, int(N**0.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    return [num for num in range(M + 1, N + 1) if array[num]]

N = int(sys.stdin.readline())
while(N != 0):
    print(len(Sieve_of_Eratosthenes(N, 2 * N)))
    N = int(sys.stdin.readline())