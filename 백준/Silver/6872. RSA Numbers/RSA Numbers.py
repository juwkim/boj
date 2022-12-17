a, b = int(input()), int(input())
ans = 0
for i in range(a, b + 1):
    ans += sum(i % d == 0 for d in range(1, i + 1)) == 4
print(f'The number of RSA numbers between {a} and {b} is {ans}')