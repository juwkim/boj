def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
def solve(num, cnt):
    if cnt == N:
        print(num)
        return
    for i in (1, 3, 7, 9):
        if isprime(num * 10 + i):
            solve(num * 10 + i, cnt + 1)
for num in (2, 3, 5, 7):
    solve(num, 1)