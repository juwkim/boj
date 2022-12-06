N = int(input())
num = N
count = 0

while(True):
    if num >= 10:
        share = num // 10
        remainder = num % 10
        num = share + remainder
        num = remainder * 10 + num % 10
    else:
        num = num * 10 + num

    count += 1
    if num == N:
        break

print(count)