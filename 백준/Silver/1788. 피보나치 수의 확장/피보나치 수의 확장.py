n = int(input())
fibo0, fibo1 = 0, 1
if n == 0 or n == 1:
    num = n
elif n > 0:
    for _ in range(n - 1):
        fibo1, fibo0 = fibo1 + fibo0, fibo1
    num = fibo1
else:
    for _ in range(-n):
        fibo0, fibo1 = fibo1 - fibo0, fibo0
    num = fibo0
print((num > 0) - (num < 0), abs(num)%(10**9), sep='\n')