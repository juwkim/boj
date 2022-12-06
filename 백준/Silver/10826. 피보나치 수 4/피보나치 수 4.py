import sys
n = int(sys.stdin.readline())

if n < 2:
    print(n)
else:
    fibo0 = 0
    fibo1 = 1
    num = 1
    for _ in range(n - 1):
        num += fibo0
        fibo0 = fibo1
        fibo1 = num
    print(num)