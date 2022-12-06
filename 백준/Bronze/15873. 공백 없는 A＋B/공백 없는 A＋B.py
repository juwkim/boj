num = int(input())
if num < 110:
    print(num // 10 + num % 10)
elif num < 1000:
    print(num // 100 + num % 100)
else:
    print(20)