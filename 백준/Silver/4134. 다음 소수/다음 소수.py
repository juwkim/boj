def isPrime(K):
    if K == 0 or K == 1:
        return False    
    for i in range(2, int(K**.5) + 1):
        if K % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())    
    while True:
        if isPrime(n):
            print(n)
            break
        n += 1