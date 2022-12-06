num = int(input())
count = 0
while num % 2 == 0:
    count += 1
    num //= 2
print(num, count)