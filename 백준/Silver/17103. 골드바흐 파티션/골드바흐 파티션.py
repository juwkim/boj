import sys

# 2 ~ N - 2 범위에 있는 소수 들을 반환
def Sieve_of_Eratosthenes(N):
    array = [True for i in range(N + 1)]
    for i in range(2, int(N**0.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    return [num for num in range(2, N - 1) if array[num]]

input()
nums = [*map(int, sys.stdin.read().split())]
primes = Sieve_of_Eratosthenes(max(nums))
for num in nums:
    
    first_index = 0
    while first_index < len(primes) and primes[first_index] <= num // 2:
        first_index += 1
        
    second_index = first_index - 1
    while second_index < len(primes) and primes[second_index] <= num - 2:
        second_index += 1
        
    first = [*reversed(primes[:first_index])]
    second = primes[first_index - 1:second_index]
    i, j = 0, 0
    count = 0
    while(True):
        try:
            if first[i] + second[j] == num:
                count += 1
                i += 1
                j += 1
            elif first[i] + second[j] > num:
                i += 1
            else:
                j += 1
        except:
            break
    print(count)