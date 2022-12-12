N = int(input())
if N % 3 == 0:
    print(3)
elif N % 4 == 0:
    print(4)
else:
    if N & 1 == 0:
        N >>= 1
    i = 3
    while i * i <= N and N % i:
        i += 2
    if i * i > N:
        i = N
    print(i)