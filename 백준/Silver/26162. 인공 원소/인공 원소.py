def isprime(num):
    if num == 1:
        return 0
    return all(num % i for i in range(2, 1 + int(num ** .5)))

for _ in range(int(input())):
    a = int(input())
    if a <= 2:
        ans = 'No'
    elif a % 2 == 0:
        ans = 'Yes'
    elif isprime(a - 2):
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)