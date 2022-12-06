N = 1000
array = [True for i in range(N+1)]
for i in range(2, int(N**.5) + 1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1
primes = [num for num in range(2, N+1) if array[num]]

for _ in range(int(input())):
    K = int(input())
    if array[K-4]:
        print(2, 2, K-4)
    else:
        K -= 3
        i = 1
        while True:
            a = primes[i]
            b = K - primes[i]
            if array[a] and array[b]:
                print(3, a, b)
                break
            i += 1