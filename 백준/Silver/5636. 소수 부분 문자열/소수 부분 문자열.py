def Sieve_of_Eratosthenes(start, N):
    array = [False, False] + [True for i in range(N-1)]
    for i in range(2, int(N**.5) + 1):
        if array[i]:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1
    return array

array = Sieve_of_Eratosthenes(0, 100000)
while N := int(input()):
    st = str(N)
    minn = min(5, len(st))
    for length in range(minn, 0, -1):
        temp = 0
        for start in range(len(st) - minn + 1):
            num = int(st[start:start+length])
            if array[num]:
                temp = max(temp, num)
        if temp:
            break
    print(temp)