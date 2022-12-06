T, count = int(input()), 0
operation, num = zip(*[input().split() for _ in range(T)])
num = [*map(int, num)]
for n in range(1, 101):
    for i in range(T):
        if operation[i][0] == 'A':
            n += num[i]
        elif operation[i][0] == 'S':
            n -= num[i]
        elif operation[i][0] == 'M':
            n *= num[i]
        else:
            n /= num[i]
        if n < 0 or n % 1:
            count += 1
            break
print(count)